# python is dynamic language that means it can reassign value

'''"""  """
variable names best pracatise pep8
strings aren't mutable(that means can't use indexing to change individual elements of a string)
type() function check data types
\n used for new line
len() for length of string or list
index means serial

slicing means grab a subsection of multiple characteres.
slice has following stucture : [start: stop: step]
string formatting:
1. format() method
2. f-strings (f)

'''
a = 444
b = a
c = b


print(" hello \n rabiul")
string = "ffdfdfad"
print(string[-3]) #index of charactar  -(minus) used for reverse index like -3 means last 3

print("slicing_Example"[3:6]) #3:6 means index start from 3 and end 6

#format
print("this is string{} ".format(":insert something"))

# serial maintain
print(" The {} {} {} {}".format("brown", "quick", "jump", "fox"))
# in {} u can index here
print(" The {1} {0} {3} {2}".format("brown", "quick", "jump", "fox"))

#f strings
name ="rabiul"
stack ="MERN"
print(f"my name is {name} and stack is {stack}")
