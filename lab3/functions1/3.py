def solve(num_heads, num_legs):
    rab = (num_legs-(2 * num_heads))/2
    chic = num_heads - rab
    return rab, chic

numheads = 35
numlegs = 94

solutions = solve(numheads, numlegs)
print(solutions)