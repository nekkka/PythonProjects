def filter_prime(numbers):
    def is_prime(n):
        if n <= 1 or n==2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    return [n for n in numbers if is_prime(n)]

a = [int(x) for x in input().split()]
# a = list(map(int, input().split()))
print(filter_prime(a))