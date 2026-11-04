"""Scope - where a variable is visible and usable
L-local = inside function
G-global = outside function
E-enclosed = nested function
B-build-in = can use everywhere"""
# x = 10
# def modify (x):
#     x = 20      #here only the inside value will  modified to modify the outside value use global
#     print(x)
# modify(x)
# print(x)


# x = 10
# def modify ():
#     global x
#     x = 20
#     print(x)
# modify()
# print(x)