# pass ka matlab kuch nai likha

class Student:
    id = 1

    def __init__(self, aname, aage, aregno, asubjects):  # used as a constructor
        self.name = aname
        self.age = aage
        self.regno = aregno
        self.subjects = asubjects

    def printing(self):
        return f"Name is {self.name}. Age is {self.age}. Registration Number: {self.regno}. Subject is {self.subjects}"

    @classmethod
    def change_id(cls, newid):
        cls.id = newid

    @classmethod
    def change_id(cls, newid):
        cls.id = newid


usman = Student("Usman", 22, "L1F19BSSE0153", "MAD")

ti = usman.printing()
print(ti)
usman.change_id(344)
print(usman.id)
