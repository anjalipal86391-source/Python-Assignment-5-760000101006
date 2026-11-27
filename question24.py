file = open("sample.txt", "r+")

data = file.read()
print("Original Content:")
print(data)

file.write("\nLearning Python is easy.")

file.close()

print("File updated successfully.")