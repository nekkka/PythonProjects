import re
text = "fgh_gh_ghkkl_fajs_afghjlkl"
def snake_to_camel(txt):
    tx = re.findall("[a-z]+",text)
    help = ""
    for i in tx:
        help+=i[0].upper()+i[1:len(i)]
    return help
print(snake_to_camel(text))
