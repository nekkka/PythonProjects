import os

# print(os.listdir(path="."))

# print(os.walk("."))

# for i in os.walk("./projects"):
#     print(i)

for dirpath, dirnames, filenames in os.walk("."):
    print ("Path: ", dirpath)
    print ("Directories: ", dirnames)
    print("Files: ", filenames)
    print()


