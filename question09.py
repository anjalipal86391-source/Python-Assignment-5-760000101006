file = open("sample.txt", "r")

word = input("Enter word to search: ")

for line in file:
    if word in line:
        print(line)

file.close()