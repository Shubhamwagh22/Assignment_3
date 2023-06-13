# Write a Python program to reverse a string.
# Note enter string as : 1234abcd

string = input("Enter the string : ")
name = " "
for i in string:
    name = i + name
print ("The reversed string is : ", name)
