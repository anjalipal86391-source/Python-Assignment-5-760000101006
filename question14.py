text = input("Enter some text: ")

file = open("usertext.txt", "w")

file.write(text)

file.close()

print("Text saved successfully.")