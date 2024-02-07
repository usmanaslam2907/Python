import time
# execution time of program
# time function in time to

initial=time.time()
print(initial)
for i in range(45):
    time.sleep(3)
    print("this is harry bhai")
print("For loo seconds is: ",time.time()-initial)

k = 0
initial2=time.time()
while k < 45:
    print("this is harry bhai")
    k=k+1
print("While loop seconds is: ",time.time()-initial2)
# localtime=time.asctime(time.localtime(time.time()))
# print(localtime)
