#Write a Python program to find the sequences of one upper case letter followed by lower case letters.


import re

txt="jabDgbsdhf abb akjabbbhkGdhnkcncki DHHah nbkaaKbbbjbh"
x=re.findall(r"[A-Z][a-z]", txt)
print(x)