import os
os.chdir('C:/Users/ASUS/Desktop/pp2/lab 6/try/')
a = ['Besh', 'Meat', 'Salad', 'Samsa', 'Cheburek', 'Pelmen']
f = open("C.txt", "a")
for i in a:
    f.write(i+' ')
f.write("\n")
f.close()
f = open("C.txt").read()
print(f)