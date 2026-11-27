import os

name = "sample.txt"

if os.path.exists(name):
    print("File exists")
    print("File size:", os.path.getsize(name), "bytes")
else:
    print("File does not exist")