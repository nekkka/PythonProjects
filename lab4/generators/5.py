def my_generator(n):
    value = n
    while value >= 0:
        yield value 
        value -= 1

n = int(input())
for value in my_generator(n):
    print(value)