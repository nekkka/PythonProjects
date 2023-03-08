import os
os.chdir('C:/Users/ASUS/Desktop/python ict/')
filename = 'assignment_6.py'
num_lines = 0

if os.path.isfile(filename):
    with open(filename, 'r') as file:
        for line in file:
            num_lines += 1
    print("Number of lines:", num_lines)
else:
    print("File does not exist.")