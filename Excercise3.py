num = 18

count = 0
while (True):
    print("Guess is left: ", 9 - count)
    if count == 9:
        print("Guesss limit is complete! Thanks")
        print("Game Over")
        break
    num = int(input("Guess the number: "))
    count = count + 1
    if num == 18:
        print("Congratulates You are successfully Guess\n")
        print("No of Guesses: ", count)
        print("<<<Game Over>>>\n")
        break
    elif num < 18:
        print("Lesser number please increase the number\n")
        continue
    elif num > 18:
        print("Greater number please decrease the number\n")
    else:
        print("Please Enter the correct number: \n")
