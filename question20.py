file = open("numbers.txt", "w")

for i in range(1, 101):
    file.write(str(i) + "\n")

file.close()

print("First 100 natural numbers saved successfully.")