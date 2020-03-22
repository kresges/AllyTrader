'''

'''
from brokerage_api import AllyAPI

class TradeFinder():
    def __init__(self):
        self.allyAPI = AllyAPI()

    def optimize_option_chain(self, ticker):
        option_chain = self.allyAPI.get_option_chain(ticker)
        print("There are {} quotes in the chain for {}".format(len(option_chain.quotes), ticker))
        print("There are {} quotes in the chain for {} with volume {}".format(len(option_chain.filter_quotes_by_volume(10)), ticker,10))

