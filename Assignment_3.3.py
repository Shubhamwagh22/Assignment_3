# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Note enter Sample String as : 'The quick Brow Fox'

string = input('Enter Sample String : ')
def up_low(string): 
    upper = []
    lower = []
    for i in string:
        if i.isupper():
            upper.append(i)
        elif i.islower():
            lower.append(i)
        else:
            pass  
    return upper, lower

upper, lower = up_low(string)        
print(f'No. of Upper case characters : {len(upper)}')
print(f'No. of Lower case Characters : {len(lower)}')
