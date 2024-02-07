# a = input("What is your name: ")
# b = input("How much do you earn")
# if int(b)==0:
#     raise ZeroDivisionError("B is zero so stopping the error")
# if a.isnumeric():
#     raise Exception("Numer are not allowed")

# General raise exception

# include question write two exception and work as a practical


"""If a required 20 sec  and b is reqired 30 sec so answer in a/b 
  so we save time we check first b is zero or not if zero so raise exception and save time of user"""

c = input("What is your name: ")
try:
    print(a)
except Exception  as e:
    if c=="harry":
        raise ValueError("Harry is blocked")

    print(" Exception handled")