def filter_prime(numbers):
    def is_prime(x):
        if x <= 2:
            return False
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    return list(filter(lambda x: is_prime(x), a))
a = [int(x) for x in input().split()]
print(filter_prime(a))