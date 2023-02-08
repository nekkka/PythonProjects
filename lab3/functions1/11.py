def palindrome(a, cnt=0):
    for i in range(len(a)):
        if a[i] == a[-i]:
            cnt += 1
    if cnt >= len(a)/2:
        return True
    else:
        return False

print(palindrome(str(input())))