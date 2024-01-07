file = open("file1.txt", "w") #create file
lines = ["hello world", "welcome to python", "enjoy learning python"] #content in file
file.writelines(lines) #print the lines
file.close()
print("data written into the file")


fout = open('output.txt', 'w')
line1 = "This here's the wattle,\n"
fout.write(line1)
x = 52
fout.write(str(x))

