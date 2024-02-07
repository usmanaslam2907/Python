# pass ka matlab kuch nai likha

class Student:
    def __init__(self, aname, aage, aregno, asubjects):  # used as a constructor
        self.name = aname
        self.age = aage
        self.regno = aregno
        self.subjects = asubjects

    def printing(self):
        return f"Name is {self.name}. Age is {self.age}. Registration Number: {self.regno}. Subject is {self.subjects}"


usman = Student("Usman", 22, "L1F19BSSE0153", "MAD")
# zeeshan = Student()

# instance ma variable dena
# usman.name = "usman"
# usman.age = 22
# usman.regno = "L1F19BSSE0153"
# usman.subjects = ["ML", "MAD"]

ti = usman.printing()
print(ti)
