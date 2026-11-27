file = open("sample.txt", "r")

lines = file.readlines()

count = len(lines)

print("Total Lines =", count)

file.close()