def histogram(a):
    for i in range(len(a)):
        print("*" * a[i])


a=list(map(int, input().split()))
print(histogram(a))