file = open("sample.txt", "r")

file.seek(6)

data = file.read()

print("Content after changing position:")
print(data)

file.close()