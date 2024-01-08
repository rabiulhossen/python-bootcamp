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