a = list(map(int, input().split()))
product = 1
for i in range(len(a)):
    product *= a[i]
print(product)
