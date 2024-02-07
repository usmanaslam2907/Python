# ls = []
# for i in range(100):
#     if i % 3 == 0:
#         ls.append(i)


# Used list comprehnsions
# ls = [i for i in range(100) if i % 3 == 0]
# print(ls)

liss = [i for i in range(100) if i % 3 == 0]
dictt = {j: f"item {j}" for j in range(10, 50) if j % 2 == 0}

# Used Dictionary Comprehensions
dict1 = {j: f"item{j}" for j in range(10, 50) if j % 2 == 0}  # good scalability
# print(dict1)

# dic2={value:key for key,value in dict1.items()}
# print(dict1,"\n",dic2)

# used set comprehensions
# dresses={dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2","dress1","dress2"]}
# print(dresses)  #set and list difference set just specific print and list print all dresses
# dresse=[dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2","dress1","dress2"]]
# print(dresse)

# used generator comprehension
evens = (k for k in range(100) if k % 2 == 0)
# print(type(evens))
print(evens.__next__())
print(evens.__next__())
print(evens.__next__())

# Question included
