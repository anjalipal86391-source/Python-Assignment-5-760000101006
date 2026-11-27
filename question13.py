file = open("multiple.txt", "w")

lines = [
    "Welcome to Python.\n",
    "Python is easy to learn.\n",
    "We are learning file handling."
]

file.writelines(lines)

file.close()

print("Multiple lines written successfully.")