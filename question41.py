import os

name = input("Enter file name: ")

if os.path.isfile(name):
    print("File exists")
else:
    print("File does not exist")