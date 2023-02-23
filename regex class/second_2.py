import re
txt="http:// defvgbhjmkhttps:// httttps://"
x=re.findall("\bhttp://|https://", txt)
print(x)