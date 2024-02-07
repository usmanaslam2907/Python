muawa = 856


def function():
    a = 5
    # b = 3
    print(a)  # first function find variable in their scope if not find else find in global
    # get permission for change muawa
    global muawa  # global keyword used for permission
    muawa = muawa + 4
    print(muawa)


# print(b)
function()


print(x)
