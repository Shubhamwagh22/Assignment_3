# Write a Python function to sum all the numbers in a list.

lst = (8,2,3,0,7)
def sum(lst):
    addition = 0
    for i in lst:
        addition += i
    return addition
total = sum(lst)
print(total)
