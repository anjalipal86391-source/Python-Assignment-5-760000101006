file = open("sample.txt", "r")

print("Initial Position:", file.tell())

file.read(10)

print("Current Position:", file.tell())

file.close()