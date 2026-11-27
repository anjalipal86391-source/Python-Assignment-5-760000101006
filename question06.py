file = open("sample.txt", "r")

data = file.read()

count = len(data)

print("Total Characters =", count)

file.close()