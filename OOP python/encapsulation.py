class BankAccount:
    def __init__(self,initial_balance):
        self.initial_balance=initial_balance
        self.public_id='123'
        self._currency="$"
        def deposite(self,ammount):
            if ammount>=0:
                self.balance+=ammount
                print(f"Deposited {ammount}. {self.balace}")
            else:
                print("INvalid deosite ammount")
        def get_balance(self):
            return self.__balance
account=BankAccount(1000)
print(f"AccountID :-{account.public_id}")
print(f"currency is:- {account._currency}")