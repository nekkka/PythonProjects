import re

txt = "FHjjk ooaujdjusbjk ab  gdhjaosifb ksdksjikdi"

x = re.findall("a+b*", txt)

print(x)
