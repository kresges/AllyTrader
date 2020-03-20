'''

'''
import json
import requests
from requests_oauthlib import OAuth1

from .brokerage_info import build_option_chain_info
from .http_utils import check_http_status, attempt_json_decode

from .secrets import CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from .brokerage_interface import BrokerageInterface

BASE_URL = 'https://api.tradeking.com/v1/'
ACCOUNT_URL = '{}/accounts.json'.format(BASE_URL)
ACCOUNT_BALANCE_URL = '{}/accounts/balances.json'.format(BASE_URL)

OPTION_CHAIN_URL = '{}/market/options/search.json'.format(BASE_URL)

class AllyAPI(BrokerageInterface):
    '''
    Ally brokerage api wrapper
    '''
    def __init__(self, getInfo=False):
        '''
        :param getInfo: Will initialize the user account number for later use.
        :type bool
        '''
        self.user = "spencer"
        self.auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        #self.info_builder = InfoBuilder()
        if(getInfo == True): self._get_account_number()

    def _get_account_number(self):
        '''
        '''
        self.account_number = self.get_account_info()['accounts']['accountsummary']['account']

    def get_user(self):
        '''
        '''
        return self.user

    def get_account_info(self):
        '''
        '''
        return requests.get(ACCOUNT_URL, auth = self.auth).json()['response']

    def get_account_balance(self):
        '''
        '''
        return requests.get(ACCOUNT_BALANCE_URL, auth = self.auth).json()['response']

    def get_account_history(self):
        '''
        '''
        if(self.account_number != None):
            account_history_url = BASE_URL + '/accounts/{}/history.json'.format(self.account_number)
            return requests.get(account_history_url, auth=self.auth).json()['response']
        else:
            return None
    
    @build_option_chain_info
    def get_option_chain(self, ticker):
        '''
        '''
        val = None
        payload = {'symbol':ticker, 'query':'strikeprice-eq:250 AND xdate-eq:20200327 AND put_call:call'}
        res = requests.get(OPTION_CHAIN_URL, auth=self.auth, params=payload)
        if( check_http_status(res) ):
            val = attempt_json_decode(res)
        return val

    
