import sys # module for path finding
# print("\n python path = \n",sys.path)

from math import pi #  import only pi
# import math # import entire math module
print(pi)

import myModule # import own module
# create a .py file and write essential code then impoort file name

n= int(input("enter a number: "))

print("factorial value", myModule.fact(n))
print("fibonacci term is ", myModule.fib(n))

def area (r):
    return (pi*r**2)

def circumference(r):
    return (2*pi*r)


print(area(3))
print("circumference is", circumference(4))



