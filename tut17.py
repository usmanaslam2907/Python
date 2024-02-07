i=0
""""
while(i<45):
    print(i)
    i=i+2"""

"""while(1):
    if i+1<5:
     i=i+1
     continue

    print(i,end=" ")
    if i==99:
        break
    i=i+1"""

while(True):
    inp = int(input("Enter a number: "))
    if inp>100:
         print("Greater than 100")
         break
    else:
         print("Try Again")
         continue