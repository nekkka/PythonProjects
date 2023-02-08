def permutation(word, permu=''):
    if len(word)== 0:
        print(permu)
    for i in range(len(word)):
        newpermu = permu + word[i]
        newword = word[0:i] + word[i+1:]

        permutation(newword, newpermu)

s=str(input())
permutation(s)