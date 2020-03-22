from trade_finder import TradeFinder

def main():
    tradeFinder = TradeFinder()
    tradeFinder.optimize_option_chain('AAPL')

if __name__ == '__main__':
    main()
