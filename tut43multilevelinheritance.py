class Dad:
    basketball = 1

class Dad:
    id=1

class Son(Dad):
    _dance

class Son(Dad):
    _dance = 1    #public

    def isdance(self):
        return f"Yes I am son and beiggest dancer {self.dance}"

class GrandSon(Son):
    # basketball=9
    __dance=6   #private

    def isdance(self):
        return f"yES I am grandson and awesome dance {self.dance}"


darry=Dad()
larry=Son()
harry=GrandSon()
print(harry.isdance())
print(harry.basketball)


# polymerisms
print(5+6)
print("5"+"6")
# there have override methods 

