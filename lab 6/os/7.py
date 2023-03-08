import os
os.chdir('C:/Users/ASUS/Desktop/python ict/')


with open('assignment_4.py', 'r') as first:
    contents = first.read()

with open('try(pp2).py', 'w') as second:
    second.write(contents)
