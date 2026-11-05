
"""POLIMORPHISM - ability to represent an object in many form
types 1. overloading --> 1.operator 2.method 3.constructure
2.overriding  --> method overriding or run time polymorphism 
3.duck typing(next slide) -->
"""

"""operator overloading - we can use the same operator or method for different purpose
(compile time polymorphism)
method overloading - if there are two or more methods in a class with the same  
name but a different number of arguments, it is known as method overloading.
python does  not support it directly.
constructor overloading - method to overload in same method or function
"""

"""method overriding - to override a  method in the parent class we need to 
redifine the  the  same method in the child class. so when the method is
called from the object of the child class  the new method will be called due to 
method resolution order (MRO)
"""
"""Duck typing - it is walks like a duck and quake like a duck ,it is a duck
python cares object not class"""

# class Dog:
#     def sound(self):
#         print('woof')
# class Cat:
#     def sound(self):
#         print('meows')

# class Duck:
#     def sounf(self):
#         print('quacks')

# # class Book: 
# #     def source(self):    #when we give non comman method it will error
# #        pass

# def speaks(animals):
#     animals.sound()

# d = Dog()
# c = Cat()
# dk = Duck()
# # b = Book()

# speaks(d)

"""MAGIC METHODS-it will call  automatically when an operation is performed
it is also called as dunder because double underscore
it's types
__init__
__del__
__str__
__repr__
__len__
__add__
__eq__   """
