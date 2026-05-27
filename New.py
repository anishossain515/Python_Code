import os
import random



# def game():
#     print('You are playing the game...')
#     score = random.randint(1,100)

#     with open('Hi-Score.txt') as f:
#         highscore = f.read()
#         if(highscore != ''):
#             highscore = int(highscore)
#         else:
#             highscore = 0
#     print(f'your score {score}')

#     if (score>highscore):
#         with open('Hi-Score.txt','w') as f:
#             f.write(str(score))
#     return score

# game()



#generate table

# def generateTable(n):
#     table=""

#     for i in range(1,11):
#         table += f'{n} x {i} = {n*i}\n'

#     with open(f'Tables/table_{n}.txt','w') as f:
#         f.write(table)

# for x in range(2,21):
#     generateTable(x)

# with open('log.txt','r') as f :
#     content = f.readlines()

# lineno= 1

# for line in content:
#     if ('python' in line):
#         print(f'yes python is present line no.{lineno}')
#         break
#     lineno +=1
# else:
#     print('python is not found')


