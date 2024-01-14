import sys # module for path finding
# print("\n python path = \n",sys.path)

from math import pi #  import only pi
# import math # import entire math module
print(pi)

def area (r):
    return (pi*r**2)

def circumference(r):
    return (2*pi*r)


print(area(3))
print("circumference is", circumference(4))


