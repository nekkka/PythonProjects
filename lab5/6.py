#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

import re

txt="jab bsdhf a/bb akjabbbh..kdhnkcn,cki nbkaabbbjbh"
x = re.sub(r"[ \,\.]", ":", txt)
print(x)