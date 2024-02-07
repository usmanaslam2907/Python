class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}.{lname}@codewithHarry.com"

    def explain(self):
        return f"This is employee is {self.fname} {self.lname} and mail is {self.email}"

    @property
    def email(self):
        if self.fname is None or self.lname is None:
            return "Email is not set in variable so using setter to set email"
        return f"{self.fname}.{self.lname}@{self.domains}"


@email.setter
def email(self,string):
    names=string.split("@")[0]
# setter function
@email.setter  # we input email so used setter
def email(self, string):
    print("setting now")
    names = string.split("@")[0]
    domains = string.split("@")[1]
    self.fname = names.split(".")[0]
    self.lname = names.split(".")[1]
    self.domains = domains


#     delete email
@email.deleter
def email(self):
    self.fname = None
    self.lname = None
    self.domains = None


pakistani_supporter = Employee("Usman", "Wains")
# pakistani_supporter.fname="us"
# print(pakistani_supporter.email)
# print(pakistani_supporter.explain())


# setter function help this line to set value otherwise take error without setter function
pakistani_supporter.email = "usman.aslam@yahoo.com"  # so used setter function
# var=pakistani_supporter.explain()
print(pakistani_supporter.email)
del pakistani_supporter.email
print(pakistani_supporter.email)
