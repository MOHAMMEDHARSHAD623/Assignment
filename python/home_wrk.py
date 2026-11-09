# def fact (n):
#     if n > 0 :
#         return "positive"
#     elif n < 0:
#         return "negative"
#     else: 
#         return "zero"

# print(fact(0))
# print(fact(-1))
# print(fact(4))

#----------------------------------------------------------------------------
# def sum_digit(n):
#     if n <= 0:
#         return "it's negative int"
#     else:
#         return (n // 33) 

# print(sum_digit(482))

#------------------------------------------------------------------------------
# def count(n):
#     if n ==  0 :
#         return 

#     print(n)
#     return count(n - 1) 
# count(10)

#-------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# f = int(input("enter the fahrenheit: "))
# c =  lambda f: (f- 32)*5/9

# print(c(f))

#-----------------------------------------------------------------------------
# words = ["p","y","t","h","o","n"]
# sorted_words = lambda x:sorted(x)

# print(sorted_words(words))

#------------------------------------------------------------------------------
# larghest_number = lambda a,b : "A is heigher"  if a>b else "B is heigher"

# print(larghest_number(20 , 300))

#----------------------------------------------------------------------------
"""------------------------------9--------------------------------------"""

"""---------------------------HOF---------------------------------------------"""

# def add(a,b):
#     return  a+b
# def sub(a,b):
#     return a-b
# def multi(a,b):
#     return a*b
# def division(a,b):
#     return a/b

# def calculator( a , b , func):
#     return func(a , b)

# print(calculator(23 , 27 , add))
# print(calculator(2 , 2  , sub))

#----------------------------------------------------------------------

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

