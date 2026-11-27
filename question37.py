file = open("sample.txt", "r")

ch = input("Enter a character: ")

for line in file:
    if line.startswith(ch):
        print(line, end="")

file.close()