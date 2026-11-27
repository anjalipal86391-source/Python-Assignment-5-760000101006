file1 = open("sample.txt", "r")
data1 = file1.read()

file2 = open("welcome.txt", "r")
data2 = file2.read()

file3 = open("merged.txt", "w")

file3.write(data1 + "\n" + data2)

file1.close()
file2.close()
file3.close()

print("Files merged successfully.")