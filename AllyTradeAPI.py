import requests
from requests_oauthlib import OAuth1
import json

from ally_api import AllyAPI
from secrets import CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET

BASE_URL = 'https://api.tradeking.com/v1/'
ACCOUNT_URL = '{}/accounts.json'.format(BASE_URL)

def testAPI():
    auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    response = requests.get(ACCOUNT_URL, auth = auth).json()

    print(response)

def main():
    print("AllyTradeAPI!")
    #testAPI()
    allyAPI = AllyAPI()
    print(allyAPI.get_user())

if __name__ == '__main__':
    main()
