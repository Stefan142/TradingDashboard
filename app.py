import os
from flask import Flask, render_template, request, session, redirect
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import requests
from helpers import login_required, handle_newsAPI
from models import db, User, APICLASS 
from datetime import datetime, timedelta
import json, csv
import configAPI

app = Flask(__name__, static_url_path='/static')


# Check for the environment variable
if not os.getenv("DATABASE_URL"):
    # If DATABASE_URL is not set, use a default value
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:HelloWorld@localhost/finalproject"
else:
    # If DATABASE_URL is set, use its value
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Configure session to use the filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# Class which functions as storage for stocks and other properties.
stocksinfo = APICLASS()


# Login.
@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("login.html", apology="Unable to login, username not submitted")

        elif not request.form.get("password"):
            return render_template("login.html", apology="Unable to login, password not submitted")

        user = User.query.filter_by(username=request.form.get("username")).first()

        if not user or not check_password_hash(user.hash, request.form.get("password")):
            return render_template("login.html", apology="Unable to login, incorrect username and/or password.")

        session["user_id"] = user.id

        return redirect("/")

    else:
        return render_template("login.html")





# Route for the dashboard.
@app.route("/", methods = ["GET", "POST"])
@login_required
def dashboard_html():
    
    # Converts all stocks in stocksinfo, to proper format.
    data = stocksinfo.convertWatchlist()

    financialsymbol = request.form.get("symbolfinance")
    user = User.query.get(session["user_id"])

    # Different scenario's depending on what is present in the object.
    if stocksinfo.checkIfInWatch(financialsymbol) and financialsymbol != None: 

        # Is needed to be able to switch the financial information in the dashboard, if in watchlist.
        index = stocksinfo.returnSymbolindex(financialsymbol)

        return render_template("dashboard.html", data = data, drawing_tool_enabled = user.drawing_tool_enabled, name = user.username, financialsymbol = data[index])
    
    elif financialsymbol != None:
        return render_template("dashboard.html", data = data, drawing_tool_enabled = user.drawing_tool_enabled, name = user.username, apology = "Not in watchlist.")
    
    else:
        return render_template("dashboard.html", data = data, drawing_tool_enabled = user.drawing_tool_enabled, name = user.username)


# Logout
@app.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    return redirect("/login")


# Registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("register.html", apology="Unable to register, username not submitted")

        elif not request.form.get("password"):
            return render_template("register.html", apology="Unable to register, Password not submitted")

        elif request.form.get("password") != request.form.get("confirmation"):
            return render_template("register.html", apology="Unable to register, Confirmation not equal to Password")

        rows = User.query.filter_by(username=request.form.get("username")).first()

        if rows is not None:
            return render_template("register.html", apology="Unable to register, username already exists")

        user = User(username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")))
        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id

        return redirect("/")
    else:
        return render_template("register.html")
    

# adds stocks to watchlist in chart on dashboard.
@app.route("/addwatch", methods=["GET", "POST"])
@login_required
def addwatch():
    if request.method == "POST":
        stock_count = request.form.get('stock_count')

        # Check if 'stock_count' is not None before converting
        if stock_count is not None:
            stock_count = int(stock_count)

        # Handle the stocks submitted by the form.
        for i in range(1, stock_count + 1):
            stock_symbol = request.form.get(f'stock{i}')
            if stocksinfo.checkIfExists(stock_symbol):
                stocksinfo.addtowatchList(stock_symbol)
            else:
                return render_template("addwatch.html", apology=f"Unable to add {stock_symbol}, Stock not listed on Alpaca")
        return redirect("/")

    return render_template("addwatch.html")


# Deletes the watchlist.
@app.route("/deletewatch")
@login_required
def deletewatch():
    stocksinfo.deleteWatchlist()
    return redirect("/")


# Toggles the drawing tool.
@app.route("/toggle-drawing-tool", methods=["POST"])
@login_required
def toggle_drawing_tool():
    
    user = User.query.get(session["user_id"])

    if request.method == "POST":
        # Toggle the drawing tool status in the database
        user.drawing_tool_enabled = not user.drawing_tool_enabled
        db.session.commit()

    # Pass the drawing tool status to the template
    return redirect("/")


@app.route("/simulation", methods=["GET", "POST"])
@login_required
def simulation():
    if request.method == "GET":
        return render_template("simulation_options.html")

    stock_symbol = request.form.get("stockSymbol")
    begin_datetime = request.form.get('beginDateTime')
    end_datetime = request.form.get('endDateTime')
    bartime = request.form.get("secondsPerBar")
    time_interval = request.form.get("intervalType")
    
    if not stock_symbol or not begin_datetime or not end_datetime or not bartime:
        return render_template("simulation_options.html", apology="Please fill in all fields.")
    
    begin_datetime = datetime.strptime(begin_datetime, "%Y-%m-%dT%H:%M")
    end_datetime = datetime.strptime(end_datetime, "%Y-%m-%dT%H:%M")

    news_items = handle_newsAPI(begin_datetime, end_datetime, stock_symbol)

    if begin_datetime.weekday() >= 5:
        return render_template("simulation_options.html", apology="Please choose begin date during weekdays.")

    if end_datetime.weekday() >= 5:
        return render_template("simulation_options.html", apology="Please choose end date during weekdays.")
    
    if stocksinfo.checkIfExists(stock_symbol) and end_datetime < datetime.now() - timedelta(minutes=15) and begin_datetime < end_datetime:

        formatted_begin_time = begin_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")
        formatted_end_time = end_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")

        new_bars_url = configAPI.ALPACA_API_BARS_URL + f'/{stock_symbol}/bars?start={formatted_begin_time}&end={formatted_end_time}&timeframe={time_interval}'
        r = requests.get(new_bars_url, headers=configAPI.HEADERS)

        data = r.json()["bars"]

        csv_file_name = "static/data/Histmarketdata.csv"

        with open(csv_file_name, mode='w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)

            csv_writer.writerow(["Timestamp", "Open", "High", "Low", "Close"])

            for i, bar in enumerate(data):
                timestamp = bar["t"]
                open_price = bar["o"]
                high_price = bar["h"]
                low_price = bar["l"]
                close_price = bar["c"]

                csv_writer.writerow([timestamp, open_price, high_price, low_price, close_price])

        return render_template("simulation.html" ,begin = begin_datetime, end = end_datetime, stock = stock_symbol, bartime = bartime, news_items=news_items[0], total_items = news_items[1])

    elif begin_datetime > end_datetime:
        return render_template("simulation_options.html", apology="Begin date should be before end date")

    elif not end_datetime < datetime.now() - timedelta(minutes=15):
        return render_template("simulation_options.html", apology="Requesting data that is too recent.")

    elif not stocksinfo.checkIfExists(stock_symbol):
        return render_template("simulation_options.html", apology=f"Unable to add {stock_symbol}, Stock not listed on Alpaca")