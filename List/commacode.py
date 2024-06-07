# Title: Comma Code
# Author: Vinit Chawda
# Date: 2nd June 2024

# Function takes a list and converts it into a string ending with ', ' where last item will end with 'and'
def list_to_string(list):
    string = ""
    if len(list) == 0:
        return ''
    elif len(list) == 1:
        return list[0]
    else:
        for i in list[:-1]:
            if type(i) == int or type(i) == type([]):
                i = str(i)
            string += i + ', '
        string += 'and '
        string += str(list[-1])
        return string
    
l = ['apples', 'bananas', 'tofu',99 , 'cats', 2]
print(list_to_string(l))
