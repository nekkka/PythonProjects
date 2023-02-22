def my_generator(a, b):
    value = 0
    for value in range (a, b):
        yield value * value
        value += 1

a = int(input())
b = int(input())
for value in my_generator(a, b):
    print(value)    