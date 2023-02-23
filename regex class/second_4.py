import re
txt="aoeuui gfhj eaeuoieu sdfapsdr"
x=re.findall(r"\b(?=\w*a)(?=\w*e)(?=\w*i)(?=\w*o)(?=\w*u)\w+\b", txt)
print(x)
