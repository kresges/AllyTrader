'''

'''
import json
import requests
from requests_oauthlib import OAuth1

from secrets import CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET

BASE_URL = 'https://api.tradeking.com/v1/'
ACCOUNT_URL = '{}/accounts.json'.format(BASE_URL)
ACCOUNT_BALANCE_URL = '{}/accounts/balances.json'.format(BASE_URL)

class AllyAPI():
    def __init__(self):
        self.user = "spencer"
        self.auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        self._get_account_number()

    def _get_account_number(self):
        self.account_number = self.get_account_info()['accounts']['accountsummary']['account']

    def get_user(self):
        return self.user

    def get_account_info(self):
        return requests.get(ACCOUNT_URL, auth = self.auth).json()['response']

    def get_account_balance(self):
        return requests.get(ACCOUNT_BALANCE_URL, auth = self.auth).json()['response']

    def get_account_history(self):
        account_history_url = BASE_URL + '/accounts/{}/history.json'.format(self.account_number)
        return requests.get(account_history_url, auth=self.auth).json()['response']

    
