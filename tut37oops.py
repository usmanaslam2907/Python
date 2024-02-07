class Employee:  # empty class denoted pass
    name = " no name"
    salary = 0
    role = " no role"
    no_of_leaves = 8
    pass


harry = Employee()
rohon = Employee()

# both objects share attributes of class so if you want change number of leaves so used
rohon.no_of_leaves = 12  # not change by this line
Employee.no_of_leaves = 10  # yes change by this line because its class attrbute not of object attribute if object attribute so like this

# take example
print(harry.__dict__)  # so no output because nor attribute of this object like output is {}
harry.gender = "Male"
print(harry.__dict__)  # but thats out put is {gender:male} because one attribute add in object

print(Employee.__dict__)  # display all attributes with values of class Employee

harry.name = "Harry"
rohon.name = "Rohon"

print(harry.name, "  ", rohon.name)
print(harry.salary, "  ", rohon.salary)
print(harry.role, "  ", rohon.role)
