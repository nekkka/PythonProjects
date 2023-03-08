import os

path = 'C:/Users/ASUS/Desktop/pp2/lab 6/byebye.txt'

# print(os.path.isabs(path))

if os.path.exists(path):
    if os.access(path, os.F_OK):
        os.remove(path)
        print('Deleted!')
else:
    print("Error")

