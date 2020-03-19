'''
    Nathanial Ziegler
    CS 5001
    February 26, 2020
    Lab 7
    Description:
    Stock
'''

def initialize_stocks(nested_list):
    ''' Name: initialize_stocks
        Parameters: nested list of lists, each nested list as ['ticker', val]
                    ticker = str and val = float
        Returns: dictionary with ticker symbol as keys, stock values as values
    '''
    stocks = {}
    for stock in nested_list:
        stocks[stock[0]] = stock[1]
    return stocks

def main():
    stocks = [['AAPL', 224.40 ], ['IBM', 140.03], ['NKE', 92.85],
              ['DIS', 129.76], ['AMZN', 1874.97], ['GOOG', 1360.66]]

    stocks_dictionary = initialize_stocks(stocks)
    
    while True:
        ticker = input("Ticker symbol? (:q:) to quit: ").upper()
        if ticker == ":Q:":
            break
        while ticker not in stocks_dictionary.keys():
            ticker = input("Invalid entry. Enter ticker symbol or (:q:) to quit: ").upper()
        print(stocks_dictionary[ticker])
        
main()
