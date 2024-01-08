"""  
file = open("file1.txt", "w")  # create file
lines = ["hello world", "welcome to python", "enjoy learning python"]  # content in file
file.writelines(lines)  # print the lines
print(list(file))
file.close()
print("data written into the file")



file2 = open("file2.txt", "r")
print(file.read(100))


print("first line:", file.readline())
print("second line:", file.readline())
file.close()
"""

file = open("file3.txt", "w")

#rename old filename
import os
# os.rename("file2.txt", "changeName.txt")
# print("file renamed")

#remove file
os.remove("file3.txt")

# try except block:

try:
    print(x)
except:
    print("print anything")
finally:
    print("print finally")
