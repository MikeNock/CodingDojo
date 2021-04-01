class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdrawal(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(self.balance)
    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        return self
acct_1 = BankAccount(0.001, 1000)
acct_2 = BankAccount(0.001, 2000)
acct_1.make_deposit(1000).make_deposit(100).make_deposit(10).make_withdrawal(500).yield_interest().display_account_info()
acct_2.make_deposit(2000).make_deposit(200).make_withdrawal(1000).make_withdrawal(1000).make_withdrawal(1000).make_withdrawal(1000).yield_interest().display_account_info()