file = open("sample.txt", "r")

data = file.read()

upper = 0
lower = 0

for ch in data:
    if ch.isupper():
        upper = upper + 1
    elif ch.islower():
        lower = lower + 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

file.close()