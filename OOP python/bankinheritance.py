class BankAccount:
    def __init__(self, acc_no, name, address, balance):
        self.acc_no = acc_no
        self.name = name
        self.address = address
        self.balance = balance

    def show_balance(self):
        print(f"Current Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}")
        self.show_balance()

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}")
        else:
            print("Insufficient balance")
        self.show_balance()

class SavingsAccount(BankAccount):
    def __init__(self, acc_no, name, address, balance):
        super().__init__(acc_no, name, address, balance)
        self.transactions = 0
        self.limit = 3

    def deposit(self, amount):
        if self.transactions < self.limit:
            super().deposit(amount)
            self.transactions += 1
        else:
            print("Transaction limit exceeded for Savings Account")

    def withdraw(self, amount):
        if self.transactions < self.limit:
            super().withdraw(amount)
            self.transactions += 1
        else:
            print("Transaction limit exceeded for Savings Account")


class CurrentAccount(BankAccount):
    def __init__(self, acc_no, name, address, balance):
        super().__init__(acc_no, name, address, balance)
        


acc_no = int(input("Enter Account Number: "))
name = input("Enter Name: ")
address = input("Enter Address: ")
balance = float(input("Enter Initial Balance: "))

print("\nChoose Account Type")
print("1. Savings Account")
print("2. Current Account")
choice = int(input("Enter choice: "))

if choice == 1:
    account = SavingsAccount(acc_no, name, address, balance)
elif choice == 2:
    account = CurrentAccount(acc_no, name, address, balance)
else:
    print("Invalid choice")
    exit()

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    option = int(input("Enter option:"))

    if option == 1:
        amt = float(input("Enter amount to deposit:"))
        account.deposit(amt)

    elif option == 2:
        amt = float(input("Enter amount to withdraw:"))
        account.withdraw(amt)

    elif option == 3:
        account.show_balance()

    elif option == 4:
        break

    else:
        print("Invalid option")
