# def function1():
#     print("Subscribe now")
# func = function1
# del function1
# func()

# def function1(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum  # sum is a function of python
#
# a = function1(0)
# print(a)
#
# def executor(func):
#     func("this")
#
# executor(print)

# ------------ Decorators -------------


#  decorators used for printer after and before the who is function like function waithing like adds

def dec1(funct):
    def nowexec():
        print("Executing Now...")
        funct()
        print("Executed...")
    return nowexec


@dec1
def who_is_usman():
    print("This is great muawa in the world that live in pakistan .")



# who_is_usman = dec1(who_is_usman)  # there have no need to write this line if we write @dec1
who_is_usman()


# easy way make 2 functions first then add decorator @

def daraz(add):
    def wrapper():
        print("scroll")
        add()
        print("executed")
    return wrapper

@daraz
def adds():
    print("adds")

adds()