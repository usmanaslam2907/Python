file = open("usman.txt")
# print(file.tell())
print(file.readline())
# print(file.tell())

print(file.seek(0))  # start and rest code according to your start index
print(file.readline())
# print(file.tell())
file.close()
