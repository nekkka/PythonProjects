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