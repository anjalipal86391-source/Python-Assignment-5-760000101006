import os

file = open("myfile.txt", "w")
file.write("Hello Students\nWelcome to Python Programming.")
file.close()

file = open("myfile.txt", "r")
data = file.read()

print("File contents:")
print(data)

file.close()

os.remove("myfile.txt")

print("File deleted successfully.")