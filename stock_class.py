from datetime import datetime
from functools import reduce


class stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.batches = []
        self.balances = []

    def buy(self, date, quantity, price):
        self.batches.append(
            {
                'date': datetime.strptime(date, '%Y-%m-%d'),
                'quantity': quantity,
                'price': price
            }
        )

    def get_month_balance(self, month, year):
        month_balance_list = list(filter(
            lambda x: x['date'].month == month and x['date'].year == year,
            self.balances
            ))
        this_month_balances = list(map(
            lambda x: x['balance'],
            month_balance_list
            ))
        if this_month_balances == []:
            return 0
        sum_monthly_balance = reduce(lambda x, y: x+y, this_month_balances)
        return sum_monthly_balance

    def sum_available_stocks(self):
        available_units = list(map(lambda x: x['quantity'], self.batches))
        sum_units = reduce(lambda x, y: x + y, available_units)
        return sum_units

    def sum_stocks_value(self):
        batch_values = map(lambda x: x['quantity'] * x['price'], self.batches)
        summed_stocks_value = reduce(lambda x, y: x+y, batch_values)
        return summed_stocks_value

    def calculate_average_price(self):
        return self.sum_stocks_value()/self.sum_available_stocks()

    def sum_total_balance(self):
        if self.balances == []:
            return 0
        batch_balance = list(map(lambda x: x['balance'], self.balances))
        summed_balances = reduce(lambda x, y: x+y, batch_balance)
        return summed_balances

    def sell(self, date, quantity, price):
        if quantity > self.sum_available_stocks():
            print("tentando vender o que não tem")
            return

        def sell_units(self, quantity_to_be_sold, price, operation_balance):
            if quantity_to_be_sold <= 0:
                # add balance
                self.balances.append(
                    {
                        'date': datetime.strptime(date, '%Y-%m-%d'),
                        'balance': operation_balance
                    }
                )
                return
            else:
                current_batch = self.batches[0]
                remaining_quantity_to_be_sold = \
                    quantity_to_be_sold - current_batch['quantity']

                price_difference = price - current_batch['price']

                if quantity_to_be_sold >= current_batch['quantity']:
                    self.batches.pop(0)
                    this_batch_balance = \
                        price_difference * current_batch['quantity']
                else:
                    self.batches[0]['quantity'] = \
                        self.batches[0]['quantity'] - quantity_to_be_sold
                    this_batch_balance = quantity_to_be_sold * price_difference

                sell_units(
                    self,
                    remaining_quantity_to_be_sold,
                    price,
                    this_batch_balance + operation_balance
                    )

        sell_units(self, quantity, price, 0)
