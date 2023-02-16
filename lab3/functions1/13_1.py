import random
                      
a=input("Hello! What is your name?")
print(f'Well, {a}, I am thinking of a number between 1 and 20. \nTake a guess')
b = random.randint(0, 20)

cnt = 1
while (True):
    s = int(input())
    if s==b:
        print(f'Good job, {a}! You guessed my number in {cnt} guesses!')
        break
    if s < b:
        print('Your guess is too low.\nTake a guess.')
        cnt += 1
    if s > b:
        print('Your guess is too big.\nTake a guess.')
        cnt += 1

    

