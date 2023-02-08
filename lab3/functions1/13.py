import random
def nice_try(s):
    if s < b:
        print('Your guess is too low.\nTake a guess.')
        
    elif s > b:
        print('Your guess is too big.\nTake a guess.')
    else:
        if s == b:
            print('Good job, '+ a+'! You guessed my number in 3 guesses!')
                
                      
a=str(input("Hello! What is your name?"))
print('Well, '+ a +', I am thinking of a number between 1 and 20. \nTake a guess')
b = random.randint(0, 20)
i = 0
while (i<=3):
    kk = int(input())
    nice_try(kk)

