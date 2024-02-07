# create library class
# methods defined
# 1. display books
# 2. lend books (if not book availabe so tell it and where is own book
# 3. add book
# 4. return books
# make class library
# constructores get
# list of books(listofbooks,libraryname)
# when we just only lend book so used """dictionary"" for name like Bookname-nameofperson is value and key is book

# create a main function and run infinite while loop for sking users for their input

class Library:
    Books = [""]
    Name = ""
    Dictionary = {"": ""}

    def __init__(self, Books, Name):
        self.Books = Books
        self.Name = Name

    def Display(self):
        print(">>>>>>>>>>>>>Display Books<<<<<<<<<<<<<<<")
        print(f"Library Name:  {self.Name}")
        print("Library Books: ", end="")
        for i in self.Books:
            print(f"{i}  ", end="")
        print("\n>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<")

    def addbooks(self,str):
        self.Books.append(str)
        print(">>>>>>>>>>>>>Book Added<<<<<<<<<<<<<<<")


    def returnbooks(self,bkname,prname):
        print("Verification Now...")
        for kk in self.Dictionary.keys():
            if kk==bkname and self.Dictionary[kk]==prname:
                del self.Dictionary[kk]
                print(f"Successfully Verified! Thanks {prname} for returning Book")
                self.addbooks(bkname)
                break
        else:
            print("Soory! Something is Wrong you are not verified")

    def lendbooks(self,booknamee,personnamee):
        for m in self.Books:
            if m==booknamee:
                self.Dictionary = {booknamee:personnamee}  # its not set its dictionary
                self.Books.remove(booknamee)
                print(f"{booknamee} Book is Borrowed by {personnamee}")
                break
        else:
            for va in self.Dictionary.keys():
                if va==bookname:
                    print(f"{va} Book is alreday Borrowed by {self.Dictionary[booknamee]}")
                    break
            else:
                print("Sorry! Book is not available in library")




if __name__ == '__main__':
    Usman = Library(["Physics", "Chemistry", "Science"], "Usman")
    while True:
        print("\n>>>>>>>Welcome Library Management System<<<<<<<<<<<<<\n")
        print("1. Display Books")
        print("2. Lend Books")
        print("3. Add Books")
        print("4. Return Books")
        print("5. Exit")

        n = int(input("\nPress Choice: "))
        if n == 1:
            Usman.Display()
        elif n == 2:
            bookname = input("Enter  BookName: ")
            personname = input("Enter Your Name: ")
            Usman.lendbooks(bookname,personname)
        elif n==3:
            bookname=input("Enter Book Name(for added): ")
            Usman.addbooks(bookname)
        elif n==4:
            bookname=input("Enter Book Name(for return): ")
            personname = input("Enter Your Name: ")
            Usman.returnbooks(bookname,personname)
        elif n == 5:
            print("\n====================================================")
            print("\n==== Thanks For Using Library Management System ====")
            print("\n====================================================")
            break
        else:
            print("Please Select Correct Option")

