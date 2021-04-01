
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        self.account_balance = amount
    def make_transfer(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

Mike = User("Mike", "mike@nockops.com")
Kaesy = User("Kaesy", "kaesy@nockops.com")
Ros = User("Ros", "roseller.yu@nockops.com")

Mike.make_deposit(10000)
Mike.make_deposit(100000)
Mike.make_deposit(1000000)
Mike.make_withdrawal(1000)
print(Mike.account_balance)
Kaesy.make_deposit(100000)
Kaesy.make_deposit(1000000)
Kaesy.make_withdrawal(1000)
Kaesy.make_withdrawal(500)
print(Kaesy.account_balance)
Ros.make_deposit(10000)
Ros.make_withdrawal(1000)
Ros.make_withdrawal(800)
Ros.make_withdrawal(600)
Mike.make_transfer(Ros, 10000)
print(Mike.account_balance)
print(Ros.account_balance)