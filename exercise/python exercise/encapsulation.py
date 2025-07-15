#create Bank class and show the encapsulation and inheritance polymorphism with deposit withdraw and function and showAccountdetails method 
class Bank:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}.New balance is{self.balance}")
        else:
            print("No money deposited")

class customer(Bank):
    def __init__(self, account_number, account_holder, balance, customer_id):
        super().__init__(account_number, account_holder , balance)
        self.customer_id = customer_id
    
    def ShowAccountDetails(self):
        print(f"Customer ID: {self.customer_id}")

