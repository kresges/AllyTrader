from .option_chain_info import OptionChainInfo
from .option_quote_info import OptionQuoteInfo

# class InfoBuilder():
#     '''
#     Info Builder!
#     '''
#     def __init__(self):
#         '''
#         '''
#         self.type = "OptionChainInfo"

def build_option_chain_info(func):
    def wrapper(self, *args, **kw):
        res = func(self, *args, **kw)

        chain_info = OptionChainInfo()

        for idx, quote in enumerate(res['quotes']['quote']):
            quote_info = OptionQuoteInfo()
            for key in quote_info.__dict__:
                quote_info.__dict__[key] = quote[key]
            chain_info.quotes[idx] = quote_info
        
        return chain_info
    return wrapper
            

