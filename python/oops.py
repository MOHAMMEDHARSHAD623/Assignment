"""FUNCTIONS ORIENTED PROGRAMMING
PROCEDURAL ORIENTED PROGRAMMING"""

"""PROGRAMMING PARADIGM
its a method or approach to  programming..."""

"""CLASS - is a  user define entity(data types)that defines the  type of data an object 
can contain and  the actions it can perform
ATTRIBUTES - DATA     METHOD - ACTIONS(function)
it doesn't uses  no memory  for data
holds no real  data"""


"""OBJECTS - it is created based on that class
create many times
hold real data
each has its own values"""

"""HOW CLASS DEFINE
1.attribute
2.method
3.object """

# class Human:
#     person1 = 'Harshad'
#     person2 = 'Ashi'

#     def done(self):
#         print('working...')   #self used for refer the current object  

# hero = Human()

# hero.done()
# print(hero.person1)
# print(hero.person2)

#----------------------------------------------------------------------------------------
# class Smartphone:
#     colour = 'burgandy colour'
#     model = '18 pro max'

#     def  phone(self):
#         print('But Venda 5K madhii')

# yasar = Smartphone()
# print(yasar.model)
# print(yasar.colour)
# yasar.phone()

#-----------------------------------------------------------------------------------------
"""Different types of Attributes
CLASS ATTRIBUTE  - IT DEFINES COMMAN DATA OF ALL ATTRIBUTES
INSTANCE ATTRIBUTE   - OBJECTS INDIVIDUAL DATA . IT DEFINES IN __init__ METHOD
LOCAL ATTRIBUTE  - USING WITHOUT SELF
"""
"""WHEN WE CREATE A OBJECT , USING __init__ (INITIALIZE METHOD )METHOD FOR CALL AUTOMATICALLY"""
#-----------------------------------------------------------------------------------------

# class Bank:
#     bank_name = 'SBI'
#     branch = 'Podanur'

#     def __init__(self, acc_number, name, ifsc):
#         self.acc_number = acc_number
#         self.name = name
#         self.ifsc = ifsc
#         self.balance = 500

#     def get_details(self):
#         print(f'Bank name:',Bank.bank_name)
#         print(f'Branch:',self.branch)
#         print(f"Account number:",self.acc_number)
#         print(f'Holder name:',self.name)
#         print(f'IFSC number:',self.ifsc)

#     def get_balance(self):
#         print(f'Balance:',self.balance)

#     def get_deposit(self):
#         amount = int(input("Enter the deposite amount: "))
#         if amount < 0 or amount <= 100:
#             print("Your amount was returned!!. please deposite amount above 100")
#         else:
#             self.balance +=  amount
#             print(f'Balance in your account is ',self.balance)

#     def withdraw(self):
#         need  = int(input("Enter the withdraw amount: "))
#         if need > 0 and  need <= self.balance:
#             self.balance -= need
#             print("Successfully withdrawen...")
#             print("Balance amount available: ",self.balance)
#         else:
#             print(f"invalid amount!!.")

# harshad = Bank(500101012440032 ,'harshad','SBI2026C05')
# adhi = Bank(12356790,'adhithyan','SBI2025C08')
# sree = Bank(1234567890,'sreeraj','SBI2020C09')

# harshad.get_details()
# harshad.get_deposit()
# harshad.withdraw()

# adhi.get_details()
# adhi.get_deposit()
# adhi.withdraw()

# sree.get_details()
# sree.get_deposit()
# sree.withdraw()

"""-----------------------------------------------------------------------------------
CLASS METHOD

declared with @classmethod decorator;the first parameter is cls(the class),not self.
can read or change class variable ;called ClassName.method

STATIC METHOD -  HELPER FUNCTION using @staticmethod decorater
takes neither self nor cls
a utility  function that belong to the class logically but does not use object or class data
"""

"""IN-BUILD class method
1.getattr -  get attribute
2.hasattr - returns true or false value , it will check the attribute is have
3.setattr -  set  attribute.  if the attribute already had it will  update otherwise it will create new
4.delattr - delete attribute . it will use for  delete attribute

print(getattr('Object name,'))
print(hasattr('oject name ,name , attribute name'))
setattr('object,name,value')
delattr('object name , name')"""

''' construtor... is a special method class that runs automattically when an object is created
used for initialize an object.

---------------------------------------------------------------------------------------------
types of constructor

default constructor - constructor with no parameters
parameterize constructor - constructor that takes parameters 
copy constructor 
'''
"""MRO = method resolution order (left to right)"""

''' destructor..... used for remove object from  memory by using __del__
they  are  called when an object gets  destroyed.
destructor are not needed as much as in C++ because python has a garbage collector that handles
'''