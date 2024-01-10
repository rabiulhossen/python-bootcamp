""" 
list is mutable means u can update it
"""

list = [3,4,5,6,78,4,46]
print(list[:-1])  #-1 indicate last index

index =0
for index in range(len(list)):
   print(list[index])
  # index = index+ list[index]
  
# input from user

talika = []

n = int(input("enter your number: "))

for i in range(n):
    new = input()
    talika.append(new) #new item added
   
    
print(talika)

list2 =[1,2,3,4]
print(list2[:2])
print(list2*3)

num =[1,4,7,4,7834,673,73,32,2,8,99]
print(num.sort()) #sort the list

#tuples
tuple =(2,3,4,5,6,)
# tuples are immutable

#set
set1 ={2,4,56,87,43}
set2 = {"a","g","gr","hfg"}

print(4 in set1)

# Write a Python program to display the sum of n numbers using a list

nums = []
num =  int(input("how many long"))

for i in range(num):
  x = int(input("enter number "))
  nums.append(x)
  
print("sum of numbers in the given list is :", sum(nums))


# Write a Python program to implement linear search on a List of elements

nums =[]
num= int(input("how many long: "))

for i in range(num):
  if (i %2 ==0):
    print( i, "is an odd number")
    
  else:
    print(i, "is even number")
