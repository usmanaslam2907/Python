var1=int(input("Enter number 1: "))
var2=int(input("Enter number 2: "))
print("Press Menu: ")
print("1: Addition: ")
print("2: Substraction: ")
print("3: Division: ")
print("4: Multiplication: ")
print("5: Exit: ")

operator=int(input("Enter Command: "))
if var1 == 45 and var2 == 3 and operator == 4:
    result=555
    print("Result is: ", result)
elif var1 == 56 and var2 == 9 and operator == 1:
    result = 77
    print("Result is: ", result)
elif operator == 4:
    print("Result is: ", var1 * var2)
elif operator == 3:
    print("Result is: ", var1 / var2)
elif operator == 2:
    print("Result is: ", var1 - var2)
elif operator == 1:
    print("Result is: ", var1 + var2)
