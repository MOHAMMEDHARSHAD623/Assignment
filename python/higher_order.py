"""------------------------HIGHER ORDER FUNCTIONS
a function that either takes another function as an argument or return a function 
as a result  or  both
funnctions that work with other functions

its functions are 
map()  do this function to every item 
filter() keep only items that pass the test
reduce()  combine all  items into one result
decoraters() changing the behaviour of function without changing its code"""

# def add (x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def multi(x,y):
#     return x*y
# def calculate(x,y,func):
#     return func(x , y)

# print(calculate(20 , 300 ,add))
# print(calculate(20 , 300 ,sub))

"""-------------------------MAP()----------------------------------"""
# def square(n):
#     return n ** 2
# numbers = [2,4,6,7,8,9]

# result = list(map(square , numbers ))
# print(result)

#----------------------------------------------------------------------
# def price(n):
#     return n * 0.9

# prices = [299,399,499,799,899,999,1099]

# result = list(map(price , prices))
# print(result)

#---------------------------------------------------------------------
# words = ['harshad','malavika','adhi','sreeraj']

# result = list(map(lambda x : x .upper(),words))  
""" #in lamba we did function and itereble"""
# print(result)

#--------------------------------------------------------------------
# numbers = [5,20,38,96,75]

# result = list(map(lambda x : x if x % 5 == 0 else 0,numbers))
# print(result)

"""----------------------------FILTER()---------------------------"""
# nums = [2,3,4,5,6,7,8,12,14,16,17]

# result = tuple(filter(lambda x : x % 2 == 0,nums))
# print(result)

#--------------------------------------------------------------------
# nums = [-5,-1,2,4,8,3,-7,-5]

# result = tuple(filter(lambda x : x >= 0 ,nums))
# print(result)

#----------------------------------------------------------------------
# wrds = ['harshad','malavika','adhi','sreeraj']

# result = list(filter(lambda  x : len(x) >= 5 ,wrds))
# print(result)

#------------------------------------------------------------------------
# wrds = ['apple','orange','banana','lemon']

# harshad = list(filter(lambda x : 'a' in x,wrds))
# print(harshad)

#------------------------------------------------------------
# wrds = ['apple','orange','banana','lemon']

# harshad = list(filter(lambda x : x.startswith ('a') ,wrds))
# print(harshad)

# wrds = ['apple','orange','banana','lemon']

# harshad = list(filter(lambda x : x[0] =='a',wrds))
# print(harshad)

"""-----------------------REDUCE()----------------------"""
# from functools import reduce

# numbs = [1,2,3,4,5,6]

# malu2 = reduce(lambda x , z : x + z , numbs )
# malu = reduce(lambda x , z : x if x>z else z  , numbs)
# print(malu)
# print(malu2)

"""-------------------------------DECORATOR-----------------------------"""
# def greet(func):
#     def does():
#         print("function started")
#         func()
#         print("ends")
#     return does

# @greet
# def on():
#     print("hello")

# on()

#-----------------------------------------------------------------
# def square(func):
#     def unsquare():
#         print("good morning everyone")
#         func()
#         print("good evening everyone")
#     return unsquare

# @square
# def hello():
#     print("good afternoon")
# hello()

#-----------------------------------------------------------------------------
# def count(n):
#     if n <= 0:
#         return n
#     print(n)
#     return count(n - 1)
# count(10)
