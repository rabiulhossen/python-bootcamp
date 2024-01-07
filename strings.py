# remove bracket from an algebraic string

def remove_brackets(str):
    for i in str:
        if i not in "()":
            print(i, end="")
    
    
    
str = input("enter any string: ")
remove_brackets(str)