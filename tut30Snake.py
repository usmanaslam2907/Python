import random

lst = ["Snake", "Water", "Gun"]
comp = random.choice(lst)
i = 0;
you = 0
computer = 0
while True:
    if i == 10:
        break
    else:
        i = i + 1
        lst = ["Snake", "Water", "Gun"]
        comp = random.choice(lst)
        print("Snake S: ")
        print("Water W: ")
        print("Gun   G: ")
        alfa = input("Enter Character: ")
        if alfa == "S" and comp == "Water":
            print("You Winner because its selected ", comp)
            you = you + 1
        elif alfa == "S" and comp == "Gun":
            print("You loser because its selected ", comp)
            computer = computer + 1
        elif alfa == "S" and comp == "Snake":
            print("Game is Tie")
            i = i - 1
        elif alfa == "W" and comp == "Gun":
            print("You Winner because its selected ", comp)
            you = you + 1
        elif alfa == "W" and comp == "Snake":
            print("You loser because its selected ", comp)
            computer = computer + 1
        elif alfa == "W" and comp == "Water":
            print("Game is Tie")
            i = i - 1
        elif alfa == "G" and comp == "Snake":
            print("You Winner because its selected ", comp)
            you = you + 1
        elif alfa == "G" and comp == "Water":
            print("You loser because its selected ", comp)
            computer = computer + 1
        elif alfa == "G" and comp == "Gun":
            print("Game is Tie")
            i = i - 1
        else:
            print("Please Select Correct Input")
            i = i - 1

if you > computer:
    print(">>>>>>>>Muawa is Winner by " , you , " Score<<<<<<<<")
    print(">>>>>>>>Computer is looser by " , computer , " Score<<<<<<<<")
else:
    print(">>>>>>>>Computer is winner by " , computer , " Score<<<<<<<<")
    print(">>>>>>>>Muawa is loser by " , you , " Score<<<<<<<<")
