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
