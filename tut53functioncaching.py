import time
from functools import lru_cache



@lru_cache(maxsize=32)
def some_work(n):
    # some task taking time
    time.sleep(n)
    return n


if __name__ == '__main__':
   print("Now running some work")
   some_work(3)   #cache data to save time and show again your data if updated so again show updated data
   some_work(1)
   some_work(6)
   some_work(1)
   some_work(4)  # deley ho ga kio k total 3+1+6+1+9=20  so 20-3(cache value) so 17 left so delay leh ga
   # if we do 32 cache value means 32 value store capable
   print("done.... calling again")
   some_work(3) # so not delay due to we used cache function
   print("Called again")

   #Question inclued


