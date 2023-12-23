# write a program to check the entered character is alphabet or digit




char = input("enter any character: ")

if char.isalpha():
    print("character is alphabret")
    
elif char.isdigit():
    print("character is digit")
    
elif char.isspace():
    print("charater is space")
    
    
letter = input("enter any character: ")

if (letter>"a") or (letter<"z"):
    print("small letter")
    
else:
    print("other")
    
    
# find the biggest number
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter second number: "))




if (a>b and a>c):
       print("a greatest",a)
    
       

elif(b>a and b>c):
    print(f"b is biggest {b}")
    
else:
    print(f"c is biggest {c}")
    
# Write a Python program to check whether the given number is even or not.
number = int(input("enter a number"))

if (number %2 == 0):
    print("this number is even", number)
    
elif(number%2 !=0):
    print("this number is odd",number)



    
    
    