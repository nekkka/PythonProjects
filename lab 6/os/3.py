import os

path = "C:/Users/ASUS/Desktop/pp2/lab5/4.py"
if(os.path.exists(path)):
    print("YES!")
    # print (os.path.basename(path), os.path.dirname(path))
    print (os.path.split(path))
else:
    print("NO!")
      

