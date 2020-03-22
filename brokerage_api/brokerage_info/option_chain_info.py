from .info_interface import InfoInterface

class OptionChainInfo(InfoInterface):
    '''
    Option chain info wrapper
    '''
    def __init__(self):
        '''
        '''
        self.quotes = {}

    def __str__(self):
        rep = ""
        for key,val in self.quotes.items():
            rep += "{} : \n {}\n".format(key, val)
        return rep

    def __repr__(self):
        rep = ""
        for key,val in self.quotes.items():
            rep += "{} : \n {}\n".format(key, val)
        return rep

    def filter_quotes_by_volume(self, volume):
        res = []
        for idx, quote in self.quotes.items():
            if int(quote.vl) >= volume:
                res.append(quote)
        return res

    def get_type(self):
        '''
        '''
        return "OptionChain"