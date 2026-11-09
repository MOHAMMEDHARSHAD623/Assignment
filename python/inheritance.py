"""INHERITANCE- it allows us to define a class that inherits all the methods and 
properties for another class we can make a another class using inheritance method
parent class - base class
child class - dirived class"""

#INHERITANCE-----------------------------------------------------------------------

# class Smartphone :
#     screen = "OLED"
#     ram ="16GB"
#     rom ="1TB"

#     def call(self):
#         print('can call')

#     def text(self):
#         print('Can message')

# class Iphone(Smartphone):
#     def camera(self):
#         print('Can capture')

# burgandy = Iphone()

# burgandy.call()
# print(burgandy.screen)

"""Types of inheritance
single  - still now we studied single 
multilevel - grand parent to parent to child
multiple - (method resolution order - MRO) one child can access multiple class 
hierarchical - one to many , single parent class inheriteed to many children class 
hybrid - combination of one or more inheritance implemented
"""
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
# class Payment:
#     def process_payment(self):
#         print('payment was processing ')

# class Method(Payment):
#     def card_payment(self):
#         super().process_payment()
#         print('card Payment')

#     def upi_payment(self):
#         super().process_payment()
#         print('Online payment')

#     def cash_payment(self):
#         print('cash on hand')
        

# m = Method()

# m.process_payment()
# m.cash_payment() 
# m.upi_payment()       

#----------------------------------------------------------------------------------
