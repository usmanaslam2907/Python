class A:
    def mett(self):
        print("This is from class A")


class B(A):
    def mett(self):
        super
        print("This is from class B")


class C(A):
    def mett(self):
        print("This is from class C")


class D(B, C):
    pass


d = D()
d.mett()
