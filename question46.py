import os

files = os.listdir("MyFolder")

print("Files present in directory:")

for name in files:
    print(name)