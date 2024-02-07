
try:
   n = int(input("Enter n of apples: "))
   mn = int(input("Enter minimum range: "))
   mx = int(input("Enter maxinmun range: "))
except ValueError:
    print("Please Enter only integer values")
    exit() #exit zaroori karna ha


if mn==mx:
    print("Error mn and mx is equal")
else:
    for i in range(mn,mx+1):
        if n%i==0:
            print(f"{i} is a divisor of {n}")
        else:
            print(f"{i} is not divisol of {n}")


