import math
import time

a = int(input("Sample Input: "))
s = int(input())
time.sleep(s/1000)

result = math.sqrt(a)

print("Square root of {} after {} miliseconds is {}".format(a ,s, result))
