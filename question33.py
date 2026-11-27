file = open("sample.txt", "r")

data = file.read()

digits = 0
special = 0

for ch in data:
    if ch.isdigit():
        digits = digits + 1
    elif not ch.isalnum() and not ch.isspace():
        special = special + 1

print("Total digits:", digits)
print("Total special characters:", special)

file.close()