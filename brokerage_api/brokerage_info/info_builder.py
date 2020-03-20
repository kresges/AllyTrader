from .option_chain_info import OptionChainInfo

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
        
        return OptionChainInfo()
    return wrapper
            

