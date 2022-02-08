from lib2to3.pgen2.parse import ParseError
import os

class Account:
    
    def __init__(self, filepath):
        if os.path.exists(filepath):
            self.filepath = filepath
            with open(filepath, 'r') as file:
                try:
                    self.balance=int(file.read())
                except ParseError:
                    print("Error!!! The balance must to be a number")
        else:
            self.balance = None

    def withdraw(self, amount):
        try:
            self.balance-=int(amount)
            self.commit()
        except ParseError:
            print("Amount mus to be a number value")

    def deposit(self, amount):
        try:
            self.balance+=amount
            self.commit()
        except ParseError:
            print("Amount mus to be a number value")

    def commit(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'w') as file:
                file.write(str(self.balance))
        else:
            print("The file was removed.")

account=Account("OOP-Example/files/balance.txt")
print(account.balance)
account.withdraw(100)
print(account.balance)
account.deposit(50)
print(account.balance)