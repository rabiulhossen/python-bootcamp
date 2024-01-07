# while loop

# syntax
# while expression:
#   statement

"""
i=7
while i>3:
    i+=1
    print(i)
    
else:
    print("no break \n")
    """

# sum of first 10 numbers

i = 1
total = 0
while i <= 10:
    total = i + total
    i = i + 1

print("sum of first 10 numbers", total, i)

n = int(input("enter any number: "))

count = 0
while n > 0:
    count = count + 1
    n = n / 10

print(count, n)


# for loop
# for var in iterable:
# statement

"""total1 = 0
for i in range[1,5]:
    total1 = total1+i
print(f"\n total is : total1")
    """


number = [1, 2, 3, 45, 5]

for num in number:
    print(num)


# find factorial of given number

n = int(input("enter a number: "))

f = 1
if n < 0:
    print("n value is must be non-nagative value")
else:
    for i in range(1, n + 1):
        f = f * i
    print("factorial is:", f)


for i in range(1, 10):
    if i == 5:
        continue
    print(i)


# cube of the number upto given an integer

number = int(input("enter a number"))
i = 1
for i in i <= number:
    print("Number is:", "i", "and cube of the:", i**3)
    i = i + 1


# display the multiplication table of a given integer or namota

num = int(input("enter the number: "))
i = 1
while i <= 10:
    print(num, "X", i, "=", num * i)
    i = i + 1
