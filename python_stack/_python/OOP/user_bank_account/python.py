class Account:
    def __init__(self, int_rate, balance, name):
        self.int_rate = int_rate
        self.balance = balance
        self.name = name
    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrew:", amount)
        return self
    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        return self
    def display_account_info(self):
        print(self.balance)
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = Account(0.001, 0, "Checking")
    def create_savings_account(self):
        self.balance = Account(0.001, 0, "Savings")
    def make_deposit(self, amount):
        self.account.balance += amount
        print(" Balance after deposit:", self.account.balance)
        return self
    def make_withdrawal(self, amount):
        if self.account.balance >= amount:
            self.account.balance -= amount
            print(" Balance after withdrawal:", self.account.balance)
            return self
        else:
            print("Insufficient Funds")
            print(" Account balance is:", self.account.balance)
    def account_yield(self):
        self.account.yield_interest()
        return self
    def display_balance(self):
        print("Your account balance is:", self.account.balance)
Mike = User("Mike", "mike@nockops.com")
Kaesy = User ("Kaesy", "kaesy@nockops.com")
Mike.make_deposit(100).make_deposit(1000).make_withdrawal(50).account_yield().display_balance()