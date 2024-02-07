file = open("usman.txt", "w")  # for write text in file and when we append then add more content
characters = file.write("Usman ak acha acha bacha ha in the world\n")
print(characters)
file.close()


file1 = open("usman1.txt", "r+")  # for write text in file and when we append then add more content
characters = file1.write("Usman ak acha acha bacha ha in the world\n")
print(characters)
file1.close()
