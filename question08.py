file = open("sample.txt", "r")

data = file.read()

words = data.split()

count = len(words)

print("Total Words =", count)

file.close()