# Recursion and iteration function k andar function
#
# def print2(str):
#     print2(str)  # function chalta rahe ga
#     print(" this is " + str)
# print2("usman")

# iterative code
n = int(input("Enter number: "))


#
# def factorial_iterative(n):
#     fact = 1
#     for i in range(n):
#         fact = fact * (i + 1)
#     return fact
#
# print(factorial_iterative(n))

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

n=int(input("Enter number: "))
print(factorial_recursive(n))
