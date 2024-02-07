# def name_printing(a,b,c,d):
#     print(a,b,c,d)
#
# name_printing("usman","zeeshan","javed","ahmad")

def funargu(normal,*args,**kwargs):
    # print(normal)
    # print(args[1])
    # print(args)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(f"{key} is a {value}")
        # print(key," and value is: ",value)
    # print(type(args))


har = ["usman", "zeeshan", "nisar", "javed","ahmad","haroon"]
norm="There are following names: "
kw={"Usman":"CR of class","Zeeshan":"Instructor","Nisar":"Cooker"}
funargu(norm,*har,**kw)   #star means pack names  ...so norm word always before
