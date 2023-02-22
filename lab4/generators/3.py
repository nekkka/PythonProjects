def three_four(x):
    value = 1
    while value < x:
        if value % 3 == 0 or value % 4 == 0:
            yield value
        value = value + 1

b = int(input())
for value in three_four(b):
    print(value)