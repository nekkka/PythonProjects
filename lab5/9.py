import re
text = "V HjAh FhjHkH"
tx = re.sub(r'(\w)([A-Z])', r'\1 \2',text)
print(tx)