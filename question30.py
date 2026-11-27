file = open("sample.txt", "r")

print("Is file closed?", file.closed)

file.close()

print("Is file closed?", file.closed)