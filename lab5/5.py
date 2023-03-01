#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

txt="as jabDgbsdhf abb akjabbbhkGdhnkcncki ahgjkb DHHah nbkaaKbbbjbh"
# txt = "avvb"

# x=re.findall(r"\ba[\w]*b\b", txt)
x=re.findall(r"\ba\w*b\b", txt)

print(x)

