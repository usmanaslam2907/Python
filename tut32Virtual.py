# enermutor

lst = ["usman", "Zeeshan", "Ahmad", "Haroon"]
i=1
for items in lst:
    if i%2!=0:
        print(f"Jarvis buy {items}")
    i=i+1

# used enermator
for index, item in enumerate(lst):
    if index % 2 != 0:
        print(f"buy please: {item}")
