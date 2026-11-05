#ABSTRACTION----------------------------------------------------
"""ABSTRACTION - abstraction is an object-oriented program concept that hides
implementation details and  shows essential features to  the user 
why it is needed
reduce complexity
improves security 
makes code easy to maintain
allows focus important features only """

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14*2**2

    def width(self):
        return 3.15*2**2

print(Circle().area())
print(Circle().width())