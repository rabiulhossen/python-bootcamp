def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


n = int(input("Enter a number: \n "))
print("factorial is ", fact(n))


# lambda function
# one line function anonymous function
# syntax
# lambda arguments: expression


def fun(f, n):
    print(f(n))


twice = lambda x: x * 2
third = lambda x: x * 3


print(fun(twice, 4))

str = "nothing to say"
upper = lambda string: string.upper()

print(upper(str))


def double(n):
    return lambda a: a * n


d = double(3)
print(d(8))



# nested function
def cube (c):
    x = c*c*c
    def square (c):
        x = c*c
        return x
    s = square(n)*c
    print(c)
    
n = int(input("enter a vlaue: "))
cube(n)


def display(name, age, salary):
    print("name", name)
    print("age", age)
    print("salary", salary)
    
    
n= "aa"
a = 20
s = 123456

display(n,a,s)