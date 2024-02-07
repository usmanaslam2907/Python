numbers = ["3", "34", "64"]

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

numbers = list(map(int, numbers))

numbers = list(map(int, numbers))


# for i in range(len(numbers)):
# #     numbers[i]=int(numbers[i])
#
# numbers=list(map(int,numbers))
#
# numbers[2]=numbers[2]+1
# print(numbers[2])

def sq(a):
    return a * a


square = list(map(sq, numbers))
square = list(map(lambda x: x * x, numbers))



#
# def square(a):
#     return a*a*a
# def cube(a):
#     return a*a*a
# func=[square,cube]
# for i in range(5):
#     val=list(map(lambda x:x(i),func))
#     print(val)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def greater_5(num):
    return num > 5


greater5 = list(filter(greater_5, list1))
print(greater5)

# -----------------------------Reduced---------------------
from functools import reduce

num = 0
list2 = [1, 2, 3, 4, 5]
num = reduce(lambda x, y: x + y, list2)
print(num)
# for j in list2:
#     num=num+j
# print(num)
