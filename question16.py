file = open("demo.txt", "w")
file.write("This is write mode.\n")
file.close()

file = open("demo.txt", "a")
file.write("This is append mode.")
file.close()

file = open("demo.txt", "r")
print(file.read())
file.close()