import re 
txt="http:// defvgbhjmkhttps://hgfjgjjhg.com fhgfhgfhf ttttps://" 
x=re.findall("\bhttp://|https://[^\s]+", txt) 
print(x)