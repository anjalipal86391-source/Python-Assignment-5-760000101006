file = open("sample.txt", "r")

data = file.read()

upper_data = data.upper()

new_file = open("uppercase.txt", "w")

new_file.write(upper_data)

new_file.close()
file.close()

print("File converted successfully.")