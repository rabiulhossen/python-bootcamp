# remove bracket from an algebraic string

def remove_brackets(str):
    for i in str:
        if i not in "()":
            print(i, end="")
    
    
    
str = input("enter any string: ")
remove_brackets(str)



def char_frequency(str1):

    dict = {}

    for n in str1:

        keys = dict.keys()

        if n in keys:

            dict[n] += 1

        else:

            dict[n] = 1

    return dict


print(char_frequency('google.com'))