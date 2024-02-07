# pass ka matlab kuch nai likha

class Student:
    id = 1

    def __init__(self, aname, aage, aregno, asubjects):  # used as a constructor
        self.name = aname
        self.age = aage
        self.regno = aregno
        self.subjects = asubjects

    def printing(self):
        return f"Name is {self.name}. Age is {self.age}. Registration Number: {self.regno}. Subject is {self.subject} and languages is {self.language}"

    @classmethod
    def change_id(cls, newid):
        cls.id = newid

    @classmethod
    def from_string_to_object(cls, string):
        return cls(*string.split("-"))  # pass as a argument/ and also used /
        # params=string.split("-")  #make a list of values and return as a object like ["zeesjan",22,"l1f19bsse0153","Math"]
        # print(params)
        # return cls(params[0],params[1],params[2],params[3])

    @staticmethod  # na class le or na hi object le like instance le just kud hi perform kare called static and used in the class Student
    def printgood(string):
        print("This is a good static method " + string)
        return "thenga"


usman = Student("Usman", 22, "L1F19BSSE0153", "MAD")
zeeshan = Student.from_string_to_object("Zeeshan-23-L1F19BSSE0156-Math")


# ti = usman.printing()
# print(ti)
# usman.change_id(344)
# print(zeeshan.printing())
# print(usman.printgood("usman"))  # also print thenga as return
# Student.printgood("Hey")   # kisi k sath b use kar sakte class ya object/instance just used for function


class programmer(Student):
    def __init__(self, name, age, regno, subject, language):
        self.name = name
        self.age = age
        self.regno = regno
        self.subject = subject
        self.language = language


nisar = programmer("Nisar", 30, "L1F19BSSE0160", "MACHINE", ["C++", "Python", "C"])
print(nisar.printing())  # print use because we return


class Players:
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printed(self):
        return f"this is the name of player is {self.name} and play game is {self.game}"

    @classmethod
    def string_to_object(cls, string):
        return cls(*string.split("/"))

rafey = Players.string_to_object("rafey/cricket")
print(rafey.printed())

class CoolProgrammer(Student,Players):
    pass

muawa=CoolProgrammer("Usman",23,"L1F19BSSE0153","GAMER")
print(muawa.printing())

