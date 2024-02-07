class Student:
    grade=4
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_data(self):
        print(f"Name is {self.name} and age is: {self.age} , grade is: {self.grade}")

    @classmethod
    def update_grade(self,g):
        self.grade=g

if __name__ == '__main__':
    s1=Student("usman",34)
    # s1.grade=9 # change just for s1 not all tak problem

    #  when i change for all
    Student.update_grade(87)
    s1.get_data()
    s2=Student("usman",34)
    s2.get_data()
    s3=Student("usman",34)
    s3.get_data()


