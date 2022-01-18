#Abstract class used to force child class to
#make method which it have
#You can't create object of abstract base class

from abc import (ABC, abstractmethod) # from this method yai apni child class ko represent kr sakti hai

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Shape):

    def __init__(self):
        self.length=6
        self.breadth=7
        # print(self.length*self.breadth)

#
    def printarea(self):  # printarea method is compulsary not you can not write print_area
        return self.length * self.breadth


a=Rectangle()
print(a.printarea())


# b=Shape()