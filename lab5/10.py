
import re

txt = "asdAsd" # -> "asd_asd" camel to snake
# txt = "asd_zxc" # -> "asdZxc" snake to camel

# x=re.findall("[A-Z]", txt)
# print(x)

s = ""
s = re.sub(r"([A-Z])", r"_\1", txt)

print(s.lower())