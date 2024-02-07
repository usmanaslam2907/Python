list1=[["usman","wains","khan"],["nisar","ahmad"],["ahmad","khan"]]
# list2=("usman","nisar","ahmad") # tuple
# for item,lollypop in list1:
#     print(item,lollypop)
# for item in list2:
#     print(item)

# convert into dictionary
dic=dict(list1)
for item,lollypop in dic.items():
    print(item,lollypop)

for item in dic:
    print(item)

items=[int,float,"usman",5,6,7,8,99,12,34,6]

for item in  items:
    if str(item).isnumeric() and item>=6:
        print(item)



