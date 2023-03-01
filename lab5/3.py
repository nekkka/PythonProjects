import re

txt="jabbsdhf abb akjabbbhkdhnkcncki nbkaabbbjbh"
txt="ab___z_asd_asdsad"
x=re.findall(r"([a-z]+)\_", txt)
print(x)