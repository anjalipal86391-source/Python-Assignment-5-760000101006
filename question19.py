num = int(input("Enter a number: "))

file = open("table.txt", "w")

for i in range(1, 11):
    file.write(str(num) + " x " + str(i) + " = " + str(num * i) + "\n")

file.close()

print("Multiplication table saved successfully.")