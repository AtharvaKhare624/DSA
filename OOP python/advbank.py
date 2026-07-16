import os
import json

class BankingSystem:
    def __init__(self, filename='accounts.json'):
        self.filename = filename
        self.accounts = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, 'r') as f:
            return json.load(f)
    
    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.accounts, f, indent=4)
            
    def create_account(self, name, initial_deposit):
        if name in self.accounts:
            print(f"Error:account for {name} already existed")
        else:
            self.accounts[name] = initial_deposit
            self.save_data()
            print(f"accounts created for {name} with ${initial_deposit}")
    
    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name] += amount
            self.save_data()
            print(f"${amount} deposited, new balace : {self.accounts[name]}")
        else:
            print("accounts not found")

    def withdraw(self, name, amount):
        if name in self.accounts:
            if self.accounts[name] >= amount:
                self.accounts[name] -= amount
                self.save_data()
                print(f"${amount} withdrawed. new balance ${self.accounts[name]}")
            else:
                print("insuffient balabce")
        else:
            print("account not found")
    
    def check_balance(self, name):
        balance = self.accounts.get(name, "account not found")
        print(f"balacne for {name}: {balance}")
    
bank = BankingSystem()

while True:
    print("\n--- Banking System Menu ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        amount = float(input("Enter initial deposit: "))
        bank.create_account(name, amount)

    elif choice == '2':
        name = input("Enter name: ")
        amount = float(input("Enter deposit amount: "))
        bank.deposit(name, amount)

    elif choice == '3':
        name = input("Enter name: ")
        amount = float(input("Enter withdraw amount: "))
        bank.withdraw(name, amount)

    elif choice == '4':
        name = input("Enter name: ")
        bank.check_balabce(name)

    elif choice == '5':
        print("Thank you for using Banking System")
        break

    else:
        print("Invalid choice, try again")