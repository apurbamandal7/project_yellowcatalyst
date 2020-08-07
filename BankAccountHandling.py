class BankAccount(object):
    balance = 0
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "The account belongs to %s and the balance is %.2f" % (self.name, self.balance)
    def showBalance(self):
        print("The balance is %.2f" % self.balance)
    def deposit(self, amount):
        if amount <= 0:
            print("You entered an invalid input.")
            return
        else:
            print("You added %.2f amount in the account." % amount)
            self.balance += amount
            self.showBalance()
    def withdraw(self, amount):
        if amount > self.balance:
            print("You don't have sufficient balance")
            return
        else:
            print("You are withdrawing %.2f amount of balance from the account." % amount)
            self.balance -= amount
            self.showBalance()

my_account = BankAccount("Kevin Dwight")
print(my_account)
deposit_amount = int(input("Enter the amount to deposit: "))
my_account.deposit(deposit_amount)
withdraw_amount = int(input("Enter the amount to withdraw: "))
my_account.withdraw(withdraw_amount)
print(my_account)