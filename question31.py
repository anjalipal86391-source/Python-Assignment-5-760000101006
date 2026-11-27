file = open("sample.txt", "r")

data = file.read()

count = 0

for ch in data:
    if ch in "aeiouAEIOU":
        count = count + 1

print("Total number of vowels:", count)

file.close()