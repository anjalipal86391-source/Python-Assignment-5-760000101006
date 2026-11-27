file = open("sample.txt", "r")

data = file.read()

word = input("Enter the word to search: ")

count = data.split().count(word)

print("Word occurrences:", count)

file.close()