file = open("sample.txt", "r")

data = file.read()

reverse_data = data[::-1]

new_file = open("reverse.txt", "w")

new_file.write(reverse_data)

new_file.close()
file.close()

print("File content reversed successfully.")