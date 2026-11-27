file = open("demo26.txt", "a+")

file.write("Welcome to Python Programming.\n")

file.seek(0)

data = file.read()

print(data)

file.close()