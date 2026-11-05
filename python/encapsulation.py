"""ENCAPSULATION - Encapsulation means wrapping data(variable) and methods(functions)
into a single unit called a class, and protecting that from being accessed directly
it allows us to control access to the data using:
1. public 
2.protected  using _(single underscore) at frnt of the name
3.private attributes using __(double underscore) at frnt of the name 
4.getter and setter - used to access private members"""

#------------------GETTER AND SETTER

class Bank:
    # class attribute
    bank_name = 'HDFC'

    def __init__(self,Holder_name, acc_number, ifsc):
        self._acc_number = acc_number
        self.holder_name = Holder_name
        self.ifsc = ifsc
        self.__balance = 0 # private member

    def get_details(self):
        print(f"Bank Name : {Bank.bank_name}")
        print(f"Holder Name : {self.holder_name}")
        print(f"Account Number : {self._acc_number}")
        print(f"IFSC Code : {self.ifsc}")

    
    def deposit(self,amount):
        if amount < 0:
            print("Enter a valid amount")
        else:
            self.__balance += amount
            print(f"Amount Deposited : {amount}")

    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient Balance..")

        else:
            self.__balance -= amount
            print(f"amount withdrawn : {amount}")


    def get_balance(self):
        print(f"Balance : {self.__balance}")

    def set_balance(self,amount):
        self.__balance = amount
        print(f"Amount {amount} updated successfully")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance = amount




arshad = Bank(123456,'arshad','SBIN00031')

print(arshad.balance)

arshad.balance = "$4000"

print(arshad.balance)   