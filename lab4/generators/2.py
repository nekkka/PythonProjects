def my_generator(n):
    value = 0
    while value < n:
        if value % 2 == 0:
            yield value
        value += 1

n = int(input())
for value in my_generator(n):
    print(value, end = ', ')