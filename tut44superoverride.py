class A:
    var1=" I am in class Variable A"
    def __init__(self):
        self.var2="Inside class A constructor"
        self.var3="game on haie bacha"
        self.special="Special"

class B(A):
    var2="I am in class B"
    def __init__(self):
        super().__init__()
        self.var2="Inside class A constructor"
        self.var3="game on haie bacha"


a=A()
b=B()
print(a)
print(b)
# print(b.special)