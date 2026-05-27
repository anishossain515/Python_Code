import random 

n = random.randint(1,50)
a = -1
guesses = 1
while(a != n):
    a = int(input('Guess the number between 1-50: '))
    if (a>n):
        print('lower number please')
        guesses += 1
    elif(a<n):
        print('higher number please')
        guesses += 1

print('Hurry! you can guess the number between {guesses} guesses')