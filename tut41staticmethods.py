
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

    @classmethod
    def change_id(cls, newid):
        cls.id = newid

    @classmethod
    def from_string_to_object(cls,string):
        return cls(*string.split("-"))  # pass as a argument/ and also used /
        # params=string.split("-")  #make a list of values and return as a object like ["zeesjan",22,"l1f19bsse0153","Math"]
        # print(params)
        # return cls(params[0],params[1],params[2],params[3])
    @staticmethod    # na class le or na hi object le like instance le just kud hi perform kare called static and used in the class Student
    def printgood(string):
        print("This is a good static method "+string)
        return "thenga"



usman = Student("Usman",22,"L1F19BSSE0153","MAD")
zeeshan=Student.from_string_to_object("Zeeshan-23-L1F19BSSE0156-Math")


ti = usman.printing()
print(ti)
usman.change_id(344)
print(zeeshan.printing())
print(usman.printgood("usman"))  # also print thenga as return
Student.printgood("Hey")   # kisi k sath b use kar sakte class ya object/instance just used for function

