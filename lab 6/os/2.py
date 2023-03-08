import os
# os.chdir('C:/Users/ASUS/Desktop/pp2/lab5')

# print(os.path.exists("C:/Users/ASUS/Desktop/pp2/lab5/6.py"))

print(os.access("C:/Users/ASUS/Desktop/pp2/lab5/666.py", os.F_OK))
print(os.access("C:/Users/ASUS/Desktop/pp2/lab5/6.py", os.W_OK))
print(os.access("C:/Users/ASUS/Desktop/pp2/lab8/6.py" , os.R_OK))
print(os.access("C:/Users/ASUS/Desktop/pp2/lab5/1.py", os.X_OK))