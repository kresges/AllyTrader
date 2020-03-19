from trade_finder import TradeFinder

def main():
    print("AllyTradeAPI!")

    #allyAPI = AllyAPI()
    tradeFinder = TradeFinder()

    print(tradeFinder._get_option_chain('AAPL'))

    #print(allyAPI.get_user())
    # print(allyAPI.get_account_balance())
    # print(allyAPI.get_account_history())

if __name__ == '__main__':
    main()
