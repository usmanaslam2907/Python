"""a = 5
b = 5
c = sum((a, b))
print(c)
"""


def average(a, b, c):
    """This is a function in which will calculate two integers"""
    result = (a + b + c) / 3
    return result


aver = average(6, 6, 6)
print("The average is: ", aver)

# that's called doc string who tell us about the function working in the  code
print(average.__doc__)

def average(a,b):
    result=a+b
    return result

print(average.__doc__)