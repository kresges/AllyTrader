'''

'''
from brokerage_api import AllyAPI

class TradeFinder():
    def __init__(self):
        self.allyAPI = AllyAPI()

    def _get_option_chain(self, ticker):
        return self.allyAPI.get_option_chain(ticker)
    
