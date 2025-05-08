import requests, json
from datetime import datetime
from flask import redirect, session
from functools import wraps




# Handles the case that a user tries to acces a route when not logged in.
def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function




# Function which returns news items as a list of dicts from the api and the number of items.
def handle_newsAPI(begin, end, symbol):
    # formatting to fit the URL.
    formatted_begin = begin.strftime("%Y-%m-%dT%H:%M:%SZ")
    formatted_end = end.strftime("%Y-%m-%dT%H:%M:%SZ")

    api_key = 'tPSrPZmCvpNa1spLnY0FZ4i5BzinenlI'
    NEWS_url = f'https://api.polygon.io/v2/reference/news?ticker={symbol}&published_utc.gte={formatted_begin}&published_utc.lte={formatted_end}&limit=1000&apiKey={api_key}'
    response = requests.get(NEWS_url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Access the content of the response and parse it as JSON
        json_data = response.json()

        # Handles the results from the JSON.
        if 'results' in json_data:
            items_count = 0
            articles = json_data['results']

            news_items = []

            for article in articles:
                title = article.get("title", "N/A")
                url = article.get("article_url", "N/A")
                description = article.get("description", "N/A")
                time_published_str = article.get("published_utc", "")
                time_published = datetime.strptime(time_published_str, "%Y-%m-%dT%H:%M:%SZ")
                
                news_item = {
                    "title": title,
                    "url": url,
                    "description": description,
                    "time_published": time_published,
                }
                news_items.append(news_item)
                items_count += 1

            return news_items, items_count
        else:
            print("No items or results found in the response.")
    else:
        print(f"Error: {response.status_code}")
