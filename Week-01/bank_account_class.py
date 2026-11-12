class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance= balance
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    def withdraw(self, amount):
        reduced_amount = self._balance - amount
        if amount > 0 and reduced_amount >= 0:
            self._balance = reduced_amount
            return True
        return False
    def get_balance(self):
        return self._balance
    def transfer(self, other_account, amount):
        if self.withdraw(amount):
            other_account.deposit(amount)
            return True
        return False  
    @property
    def balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        if rate >=0:
            self._balance = self._balance * ((rate/100)+1)
            
            return True
        return False

class LimitedAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 500:
            return False
        return super().withdraw(amount)
            

account = BankAccount("Anna", 100)

assert account.balance == 100

account.deposit(50)
assert account.balance == 150

account.withdraw(30)
assert account.balance == 120

assert account.get_balance() == 120

print("All tests passed!")