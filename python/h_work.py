
# balance = 10000
# pin = 2468

# total_deposit = 0
# total_withdrawal = 0
# transaction_count = 0

# transactions = []

# print("================================")
# print("       WELCOME TO ATM")
# print("================================")


# attempts = 0

# while attempts < 3:
#     entered_pin = int(input("Enter your PIN: "))

#     if entered_pin == pin:
#         print("\nLogin Successful!")
#         break
#     else:
#         attempts += 1
#         print("Incorrect PIN!")
#         print("Attempts remaining:", 3 - attempts)

# if attempts == 3:
#     print("\nYour account access is denied.")
# else:

#     while True:

#         print("\n========== ATM MENU ==========")
#         print("1. Check Balance")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Transaction History")
#         print("5. Exit")
#         print("==============================")

#         choice = int(input("Enter your choice: "))

        
#         if choice == 1:
#             print("\nYour Current Balance: ₹", balance)

#         elif choice == 2:
#             amount = float(input("Enter deposit amount: ₹"))

#             if amount > 0:
#                 balance += amount
#                 total_deposit += amount
#                 transaction_count += 1

#                 transactions.append(
#                     f"Deposited: ₹{amount}"
#                 )

#                 print("Amount deposited successfully!")
#                 print("Updated Balance: ₹", balance)

#             else:
#                 print("Invalid deposit amount!")

#         elif choice == 3:
#             amount = float(input("Enter withdrawal amount: ₹"))

#             if amount > 0 and amount <= balance:
#                 balance -= amount
#                 total_withdrawal += amount
#                 transaction_count += 1

#                 transactions.append(
#                     f"Withdrawn: ₹{amount}"
#                 )

#                 print("Please collect your cash.")
#                 print("Updated Balance: ₹", balance)

#             elif amount <= 0:
#                 print("Invalid withdrawal amount!")

#             else:
#                 print("Insufficient Balance!")

        
#         elif choice == 4:
#             print("\n====== TRANSACTION HISTORY ======")

#             if len(transactions) == 0:
#                 print("No transactions available.")

#             else:
#                 for transaction in transactions:
#                     print(transaction)

    
#         elif choice == 5:
#             print("\n====== FINAL TRANSACTION SUMMARY ======")

#             print("Total Deposits: ₹", total_deposit)
#             print("Total Withdrawals: ₹", total_withdrawal)
#             print("Total Transactions:", transaction_count)
#             print("Final Balance: ₹", balance)

#             print("\nThank you for using our ATM!")
#             print("========================================")
#             break

#         else:
#             print("Invalid choice! Please select 1 to 5.")

#---------------------------------------------------------------------------

# class Employee:
#     def __init__(self,name,emplyee_id,basic_salary):
#         self.name = name
#         self.employee_id = emplyee_id
#         self.basic_salary = basic_salary

#     def display_employee(self):
#         print(f'Employee name:{self.name}' )
#         print(f'Employee id: {self.employee_id}')
#         print(f'Basic salary: {self.basic_salary}')

# class Manager(Employee):
#     def __init__(self,name,employee_id,basic_salary,team_size):
#         super().__init__(name,employee_id,basic_salary)
#         self.team_size = team_size

#     def display_manager(self):
#        self.display_employee()
#        print(f'team size:{self.team_size}')
         
         
         

# m = Manager('harshad',23456,98766,5) 
# m.display_manager()

#---------------------------------------------------------------------------------

# class Vehical:
#     brand = 'SUZUKI'
#     register_code = 'KL 11'

#     def travel(self):
#         print('Can travel')

#     def  model(self):
#         print('AUDI')

# class Car(Vehical):
#     def model(self):
#         super().model()
#         print('GRAND VITARA')


# c = Car()

# c.model()

#--------------------------------------------------------------------------------
class Payment:
    def buy(self):
        print('can buy using GPAY payment method ')
        