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
            return {
                'month': f'{month}/{year}',
                'balance': 0,
                '20k_DARF': False
            }

        sold_amount_map = map(
            lambda x: x['price'] * x['quantity'], 
            sell_transactions
            )
        this_month_total_amount = reduce(lambda x, y: x+y, sold_amount_map)

        balaces_map = map(lambda x: x['balance'], sell_transactions)
        this_month_balance = reduce(lambda x, y: x+y, balaces_map)

        this_month_results = {
            'month': f'{month}/{year}',
            'balance': this_month_balance,
            '20k_DARF': this_month_total_amount >= 20000
        }
        return this_month_results

    def get_year_results(self, year):
        months_list = [i for i in range(1,13)]
        results_list = list(
            map(
                lambda x: self.get_month_balance(x, year),
                months_list
                )
            )
        
        return results_list
