# pass ka matlab kuch nai likha

class Student:
    id=1
    def __init__(self,aname,aage,aregno,asubjects):  # used as a constructor
        self.name=aname
        self.age=aage
        self.regno=aregno
        self.subjects=asubjects


    def printing(self):
        return f"Name is {self.name}. Age is {self.age}. Registration Number: {self.regno}. Subject is {self.subjects}"

    def __add__(self, other):
        return self.sala



usman = Student("Usman",22,"L1F19BSSE0153","MAD")
