"""-------------types of  function-----------------
build-in --  we already studied (add,remove....)
user defined -- defining (def....)
recursive
lambda
higher order
"""

"""---------------------recursive"""

# def count(n):
#     if n == 1:
#         return 1 

#     return n * count(n - 1)
# print(count(5))

"""-----------------------fibonacci------------------------------------"""
# def count(n):
#     if n == 0:
#         return 

#     print(n)
#     return count(n - 1)
# count(10)

"""---------LAMBDA---------------- 
it  was a one line fuction without name. we can add multiple parameters 
but only one expression
syntax <
name = lambda x,y : x+y
print(name(1,2)) > """

"""----------------------------------------------------"""
# adding = lambda b,d : b+d
    
# print(adding(2 , 3))

"""------------------------------------------------"""
# square = lambda a : a**2

# print(square(5))

"""-------------------------------------------------------"""
# typ = lambda n: "even" if n  % 2 == 0 else "odd"

# print(typ(25))

"""--------------------------------------------------------------"""
# large = lambda a , b : "a is largest " if a>b else "b  is largest"
# print(large(50 , 300))

"""---------------------------------------------------------"""
# a = int(input("enter the value: "))
# length = lambda x : x/100 #changing CM to M
# print(length(a))

"""------------------------------------------------------------"""
# hr = float(input("enter the hours: "))
# hours  = lambda x : x * 60

# print(hours(hr))

"""-----------------------------------------------------------------"""
# hr = float(input("enter the hours: "))
# hours  = lambda x : x * 3600

# print(hours(hr))