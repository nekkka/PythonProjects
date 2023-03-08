import os
os.chdir('C:/Users/ASUS/Desktop/pp2/lab 6/try/')
food = ['Besh', 'Meat', 'Salad', 'Samsa', 'Cheburek', 'Pelmen']
with open('A.txt', "w") as myfile:
        for i in food:
                myfile.write("%s\n" % i)
content = open('A.txt')
print(content.read())