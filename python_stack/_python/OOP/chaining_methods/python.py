
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)
    def make_transfer(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
Mike = User("Mike", "mike@nockops.com")
Kaesy = User("Kaesy", "kaesy@nockops.com")
Ros = User("Ros", "roseller.yu@nockops.com")
Ros.make_deposit(10000).make_withdrawal(1000).make_withdrawal(800).make_withdrawal(600)
Mike.make_deposit(10000).make_deposit(100000).make_deposit(1000000).make_withdrawal(1000).display_user_balance()
Kaesy.make_deposit(100000).make_deposit(1000000).make_withdrawal(1000).make_withdrawal(500).display_user_balance()
Mike.make_transfer(Ros, 10000).display_user_balance()
Ros.display_user_balance()