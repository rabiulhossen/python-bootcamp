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

n= int(input("enter any number: "))

count =0
while (n>0):
    count = count+1
    n = n/10
    
print(count, n)
    