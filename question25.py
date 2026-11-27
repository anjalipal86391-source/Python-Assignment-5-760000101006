file = open("demo25.txt", "w+")

file.write("Welcome to Python Programming.")

file.seek(0)

data = file.read()

print(data)

file.close()