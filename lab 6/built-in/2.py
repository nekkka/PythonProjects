s = input()
cnt_upp = 0
cnt_low = 0
for i in range(len(s)):
    if ord(s[i]) >= 65 and ord(s[i]) <= 90:
        cnt_upp+=1
    if ord(s[i]) >= 97 and ord(s[i]) <= 122:
        cnt_low+=1


print("Upp:{}\nLow:{}".format(cnt_upp, cnt_low))
