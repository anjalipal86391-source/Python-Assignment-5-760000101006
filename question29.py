file = open("sample.txt", "r")

file.seek(14)

data = file.read()

print("Content from specified position:")
print(data)

file.close()