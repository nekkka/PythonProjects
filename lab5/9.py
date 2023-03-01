import re
text = "V HjAh gjFhjHkH"
tx = re.sub(r'(\w)([A-Z])', r'\1 \2',text)
print(tx)