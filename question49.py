import os

os.rename("sample.txt", "renamed.txt")

file = open("renamed.txt", "r")

data = file.read()

print("File contents:")
print(data)

file.close()