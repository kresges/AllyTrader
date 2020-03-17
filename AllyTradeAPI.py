from ally_api import AllyAPI

def main():
    print("AllyTradeAPI!")

    allyAPI = AllyAPI()
    print(allyAPI.get_user())
    print(allyAPI.get_account_balance())
    print(allyAPI.get_account_history())

if __name__ == '__main__':
    main()
