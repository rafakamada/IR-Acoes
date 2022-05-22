from datetime import datetime
from functools import reduce
from stock_class import stock

class stock_wallet:
    def __init__(self):
        self.stock_dict = {}
        self.transactions = []
        
    def write_transaction(self, date, ticker, quantity, price, balance):
        self.transactions.append(
            {
                'date': datetime.strptime(date, '%Y-%m-%d'),
                'ticker': ticker,
                'buy_or_sell': 'buy' if quantity > 0 else 'sell',
                'quantity': quantity,
                'price': price,
                'balance': balance
            }
        )
    
    
    def buy(self, date, ticker, quantity, price):
        ticker = ticker.upper()
        if ticker not in self.stock_dict:
            self.stock_dict[ticker] = stock(ticker)
        
        self.stock_dict[ticker].buy(date, quantity, price)
        self.write_transaction(date, ticker, quantity, price, 0)
        
    def sell(self, date, ticker, quantity, price):
        ticker = ticker.upper()
        if ticker not in self.stock_dict:
            print('fodeu')
        
        self.stock_dict[ticker].sell(date, quantity, price)
        operation_balance = self.stock_dict[ticker].balances[-1]['balance']
        self.write_transaction(date, ticker, -quantity, price, operation_balance)
        

    def get_month_balance(self, month, year):
        month_transaction_list = list(filter(lambda x: x['date'].month == month and x['date'].year == year, self.transactions))
        this_month_balances = list(map(lambda x: x['balance'], month_transaction_list))
        if this_month_balances == []:
            return 0
        month_balance = reduce(lambda x,y: x+y, this_month_balances)
        return month_balance    

    
    def get_month_transactions(self, month, year):
        month_transaction_list = list(filter(lambda x: x['date'].month == month and x['date'].year == year, self.transactions))
        return month_transaction_list
    
    def get_month_balance(self, month, year):
        month_transaction_list = self.get_month_transactions(month, year)
        sell_transactions = list(filter(lambda x: x['buy_or_sell'] == 'sell', month_transaction_list))
        if sell_transactions == []:
            return 0
        balaces_list = list(map(lambda x: x['balance'], sell_transactions))
        return reduce(lambda x,y: x+y, balaces_list)
