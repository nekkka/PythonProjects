import math
def volume(rad):
    return 4/3 * 3.14*math.pow(rad, 3)

print(round(volume(int(input()))))
