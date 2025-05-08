from flask_sqlalchemy import SQLAlchemy
import alpaca_trade_api as tradeapi
import configAPI

db = SQLAlchemy()

# User model in database.
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    hash = db.Column(db.String)
    drawing_tool_enabled = db.Column(db.Boolean, default=False)

# the APICLASS used in main.
class APICLASS:

    def __init__(self):
        # connect the API to the class.
        self.api = tradeapi.REST(configAPI.ALPACA_API_KEY, configAPI.ALPACA_API_SECRET_KEY, configAPI.ALPACA_API_BASE_URL)
        self.stockList = []
        # list of all stock objects on ALPACA
        self.allstocks = self.api.list_assets()  
        self.stocksymbols = []

        # Making list of stockSymbol names.
        for stock in self.allstocks:
            self.stocksymbols.append(stock.symbol)
        

    # Adds stock to stocklist.
    def addtowatchList(self, symbol):
        if symbol in self.stocksymbols and symbol not in self.stockList:
            self.stockList.append(symbol)

    # Deletes stocks from stocklist.
    def deleteWatchlist(self):
        self.stockList = []

    # Converts the watchlist to a format understoond by the tradingview widget.
    def convertWatchlist(self):
        watchList = []
        for stock in self.stockList:
            data = self.api.get_asset(stock)
            symbol = data.__getattr__('symbol')
            exchange = data.__getattr__('exchange')

            x = str(exchange + ':' + symbol)
            watchList.append(x)
        return watchList
    
    # Checks if symbol is in the watchlist.
    def checkIfInWatch(self, symbol):
        if symbol in self.stockList:
            return True
        else:
            return False
    
    # Returns the index at which the symbol is stored in the watchlist.
    def returnSymbolindex(self, symbol):
        return self.stockList.index(symbol)
    
    # Checks if a stock exists.
    def checkIfExists(self,symbol):
        if symbol in self.stocksymbols:
            return True
        else:
            return False
    
    # Returns all symbols.
    def getallsymbols(self):
        return self.stocksymbols