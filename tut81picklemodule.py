import pickle  #achaar khana ha with chawal
#there have 5 minutes waste to list data maintain

#
# cars=["Audi","BMW","Landcrusier"]  # preserved list in file ya list b hosaktab ta kuch b ho sakta ta object tule dictionary
# # pack list in file
# file="mycar.pkl"
# fileobj=open(file,'wb')     #wb karna ha kio k binary write hota ha
# pickle.dump(cars,fileobj)  #so we savelist in file 1.List arguments  2. File where stored
# fileobj.close()


# Depickle the file
# read the file
file="mycar.pkl"
fileobj=open(file,'rb')
mycar=pickle.load(fileobj)
print(mycar)
print(type(mycar))

