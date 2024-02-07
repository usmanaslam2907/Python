"""Some function taking more time  so we need to run at one time half and
 after some time if i want to try again run function so left half function is agian running
 """

# make coroutine this is coroutine......not function
def searcher():
    import time
    # take some time like 4 second to read string
    book="This is muhammad Usman aslm wains from university of central punjab"
    time.sleep(4)
    while True:
        text=(yield)
        if text in book:
            print("Your text in the book")
        else:
            print("Your Text is not in the book")

search=searcher()
print("Search is Started")
next(search)
print("Next started")
search.send("Usman")
input("Press any key")

print("close coroutine")
search.close()

#Question Included


