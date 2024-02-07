from abc import ABCMeta, abstractmethod
# from abc import ABC,abstractmethod  same working
#  abstract class used

# class Shape(ABC):
class Shape(metacXlass=ABCMeta):

    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Shape):
    type = "rectangle"
    slides = 4
    def __init__(self):
        self.length=6
        self.breadth=7

    def printarea(self):
        return 0

rect1=Rectangle()
