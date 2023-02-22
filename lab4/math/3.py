from math import tan
def poly(n, l):
    apothem = l/(2* int(tan(180/n)))
    return n * l * apothem / 2


print(poly(4, 25))