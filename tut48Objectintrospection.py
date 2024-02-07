class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}.{lname}@codewithHarry.com"

    def explain(self):
        return f"This is employee is {self.fname} {self.lname} and mail is {self.email}"


#  object introspection
skillf=Employee("Skill","f")
# print(skillf.email)
# print(type(skillf))
# # used object introspection
# print(id("this is a strin"))
# print(id("this is a strin"))  #same id for same
# o ="this is muawa"
# print(dir(o))
# print(dir(skillf))
#
# type
# id
# dir
import inspect
print(inspect.getmembers(skillf))

