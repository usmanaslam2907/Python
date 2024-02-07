# file = open("usman.txt", "rt")
# # print(file.readlines())
# print(file.readline())
# file.close()

# Easy method
with open("usman.txt") as file:  # there have no need to close the file when we use with
    content = file.read()
    print(content)

