"""
Iterable - __iter__() or __getitem__() if varibale iterate the values so iterable
Iterator == __next__()
Iteration
"""


# for i in range(5):   #on the fly generate value iterate the value  and range is gerentor so just one time genaerte
#     print(i)

# def gen(n):
#     for j in range(n):
#         yield j
#
#     g = gen(3)  #so very important to save ram burden just we generate the variable
#     # like sonee ka anda dene wali murgi jab use ho ga tab la lu ga.....generators iterator hotain haie jinhee ap ak dafa generate kar saktain haie
#     print(g)
#     print(g.__next__())

h="harry"  # string is iterable  so whatever when i want so used __iter__()
# for i in h:
#     print(i)
it=iter(h)
print(iter.__next__())
print(iter.__next__())