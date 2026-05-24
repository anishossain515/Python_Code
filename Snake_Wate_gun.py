import random
"""
1 for Sanke
-1 for Water
0 for gun
"""
#user and computer input
Computer = random.choice([-1,0,1])
user = input('Enter you choice: ')

#convert user input to sanke/water/gun
userDict = {'s':1, 'w':-1, 'g':0}
userValue = userDict[user]

#reverse number to sanke/water/gun
reverseDict ={1:'Snake', -1:"Water", 0:"gun"}

print(f'You choose {reverseDict[userValue]}\ncomputer choose {reverseDict[Computer]}') #print what you and computer chose


if (Computer == userValue):
    print('Its draw')
else:
    if(Computer == 1 and userValue == 0):
        print('You win!')
    elif(Computer == 1 and userValue == -1):
        print('You Lose!')
    elif(Computer == 0 and userValue == 1):
        print('You Lose!')
    elif(Computer == 0 and userValue == -1):
        print('You win!')
    elif(Computer == -1 and userValue == 1):
        print('You win!')
    elif(Computer == -1 and userValue == 0):
        print('You Lose!')
    else:
        print('Something is worng')





