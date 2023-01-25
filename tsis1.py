#Python syntax
print ("Hello World")
if 5 > 2:
    print("Five is greater than two!")

#Python comments
# This is a comment

"""

This is a comment
written in 
more than just one line
"""
#Python variables
carname = "Volvo"

x=50

x = 5
y = 10
print(x + y)

x = 5
y = 10
z = x + y
print(z)

myfirst_name = "John"

x = y = z = "Orange"


def myfunc():
    global d
    d = "fantastic"


x = 5
print(type(x))   
#int

x = "Hello World"
print(type(x))
#str

x = 20.5
print(type(x))
#float

x = ["apple", "banana", "cherry"]
print(type(x))
#list

x = ("apple", "banana", "cherry")
print(type(x))
#tuple

x = {"name" : "John", "age" : 36}
print(type(x))
#dict

x = True
print(type(x))
#bool


#Python numbers
x = 5
x = float (x)

x = 5.5
x = int (x)

x = 5
x = complex (x)

#Python strings

x = "Hello World"
print (len(x))

txt = "Hello World"
x = txt[0]

txt = "Hello World"
x = txt[2:5]

txt = "Hello World"
x = txt.strip() #Return the string without any whitespace at the beginning or the end.

txt = "Hello World"
txt = txt.upper()

txt = "Hello World"
txt = txt.lower()

txt = "Hello World"
txt = txt.replace("H", "J")


age = 36
txt = "My name is John, and I am {} "
print(txt.format(age))

