f1 = open("usman.txt")

try:
    f = open("does.txt")
except Exception as e:
    print(e)
except EOFError as e:
    print("EOF Error is  here", e)
except IOError as e:
    print("IOError is here",e)
else:
    print("This is will run only if except is not running")  #except and else ma sa ak chalain ga
    # so if except working so else not working and vise versa
# finally measns k ya hona hi ha
finally:  # used for code cleaning
    print("Run any way.....")
    f1.close()    # cleanup karne k lie use karte haie like close all file which are open here

print("Important stuff here")