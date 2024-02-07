# non-volatile(HardDisk) save data if shut down laptop and volatile(RAM) not save data if shut down laptop
# read mode == open file for reading   "r"
# Write mode == open file for writing  "w"
# Create file if not exists already == "x"
# Append file means to add more content in file == "a"
# Text file mode open file ==          "t"
# binary file mode            ===       "b"
# both file read and write ====  "+"
# default mode is read and text mode


# file pointer return
# file = open("usman.txt")
file=open("Usman.")
file = open("usman.txt", "r")  # Second argument is always mode and when we add b so display in binary form
# content = file.read(3)
# print(content)
# print(file.read())

# for line in file:
#     print(line, end="")
# print(file.readline())

# for line in content:
#     print(line)
file.close()
