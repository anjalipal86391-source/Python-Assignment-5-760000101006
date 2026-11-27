import os

name = input("Enter file name: ")

if os.path.exists(name):
    print("File name:", os.path.basename(name))
    print("File size:", os.path.getsize(name), "bytes")
    print("Absolute path:", os.path.abspath(name))
else:
    print("File does not exist")