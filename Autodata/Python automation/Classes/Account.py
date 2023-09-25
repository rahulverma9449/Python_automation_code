import random

class Account(object):
    def __init__(self, user_id, currency='USD'):
        self.user_id = user_id
        self.currency = currency
        self.current_balance = self.__read_balance_from_database()
        print(f"Current balance is: {self.current_balance}")


    def withdraw(self, amount):
        self.current_balance = self.current_balance - float(amount)
        print(f"New balance after withdraw: {self.current_balance}")


    def deposit(self, amount):
        self.current_balance = self.current_balance + float(amount)
        print(f"New balance after deposit: {self.current_balance}")


    def generate_statement(self, start_date, End_date):
        pass

    def __read_balance_from_database(self):
        print(f"getting balance from db for : {self.user_id}")
        return random.randint(100, 1000)

account1 = Account(9871)
import pdb; pdb.set_trace()