def unique(num):
    b = []
    for i in num:
        if i not in b:
            b.append(i)
    return b

a = list(map(int, input().split()))
print(unique(a))