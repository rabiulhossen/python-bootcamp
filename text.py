car= {
    "model": 123,
    "name": "bmw"
}

print(car.items())

print("bib".find('b', 1, 2))
index = "Ability is a poor man's wealth".find("W")
print("%s %d %f" % (5, 5, 5))



d = {
    "model": 123,
    "name": "bmw"
}


# reversed dictionary

result = dict()
for key in d:
    val = d[key]
    if val not in result:
        result[val] = [key]
    else:
        result[val].append(key)
        

n = 10000
count = 0
while n:
    count = count + 1
    n = n // 10

print (count)

pi = float(3.14159)
print (pi)

def test_function( length, width, height):
    print ("the volume of the box is ",length*width*height)
    return length*width*height

l = 12.5
w = 5
h = 2
test_function(l, w, h)

mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
a=0
while a < 7:
    print (mylist[a],)
    a += 2
    
def area(l, w):
    temp = l * w;
    return temp

l = 4.0
w = 3.25
x = area(l, w)
if ( x ):
  print (x)
  """
try:
    fin = open('answer.txt')
    fin.write('Yes')
except:
    print('No')
print('Maybe')

fin = open('words.txt')
for line in fin:
    word = line.strip()
    print(word)

"""
print(not(True or False))

def myf(s, n):

    i =2

    print(s * i * n)


     
print("bib".find('b', 1, 2))
print ("%s %d %f" % (5, 5, 5))

mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
a=0
while a < 8:
    print(mylist[a],)
    a = a + 2

def recurse(a):
    if (a == 0):
        print(a)
    else:
        recurse(a) 

print("recurse is",recurse(0))



n = 10
while n != 1:
    print (n,)
    if n % 2 == 0: # n is even
        n = n // 2
    else: # n is odd
        n = n * 3 + 1
  
my_list = [3, 2, 1]
print(my_list)


mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
a=0
while a < 8:
    print(mylist[a],)
    a = a + 2


def recurse(a):
    if (a == 0):
        print(a)
    else:
        recurse(a) 

print(recurse(0))

  

