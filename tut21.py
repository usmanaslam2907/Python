print("Enter num1: ")
num1 = input()
print("Enter num2: ")
num2 = input()
try:
    print("Sum is: ", int(num1) + int(num2))
except Exception as e:
    print(e)

print("This is line very important! Thanks")
# why we use try and except in the code because we want to complete run the code without stop...causes of error
