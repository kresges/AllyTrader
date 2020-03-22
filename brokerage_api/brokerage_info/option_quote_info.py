from .info_interface import InfoInterface

class OptionQuoteInfo(InfoInterface):
    '''
    Option Quote info wrapper
    '''
    def __init__(self):
        '''
        '''
        self.ask = None
        self.bid = None
        self.vl = None
        self.contract_size = None
        self.days_to_expiration = None
        self.last = None
        self.opn = None
        self.prem_mult = None
        self.put_call = None
        self.rootsymbol = None
        self.strikeprice = None
        self.xdate = None
        self.xday = None
        self.xmonth = None
        self.xyear = None

    def get_type(self):
        '''
        '''
        return "OptionQuote"