file = open("sample.txt", "r")

data = file.read()

word = input("Enter the word to search: ")

if word in data:
    print("Word exists in the file")
else:
    print("Word does not exist in the file")

file.close()