# #boy or girl... if the total number of distinct character is odd he is a male otherwise a girl
# name = input('').lower()

# if name == '':
#     print('Enter a valid name')

# else:
#     Char_of_name = [] #divide the name into single character
#     for i in range(len(name)):
#         Char_of_name.append(name[i])


#     new_list_char = []

#     for word in Char_of_name: #a = list(dict.fromkeys(Char_of_name))  #remove all the same character
#         if word not in new_list_char:
#             new_list_char.append(word)

#     if(len(new_list_char) % 2 != 0):
#         print('IGNORE HIM!') #cause he is a male
#     else:
#         print('CHAT WITH HER!')#cause she is a girl


# n = int(input())

# for _ in range(n):  
#     word = input() 

#     if (len(word) > 10):
#         new_word = word[1:-1]
#         print(f'{word[0]}{len(new_word)}{word[-1]}')
#     else:
#         print(word)

#proble name --Team

#my solution
# n = int(input())

# total = 0

# for _ in range(n):
#     user_input = input()

#     number_list = []

#     for x in user_input:
#        number_list.append(int(x))

#     number_of_solution = 0

#     for i in number_list:
#        if (i == 1):
#          number_of_solution+=1

#     if (number_of_solution >=2): 
#        total += 1
    
# print(total)

#real solution
n = int(input())

total = 0

for _ in range(n):
    user_input = input().split()

    number_list = []

    for x in user_input:
        number_list.append(int(x))

    number_of_solution = 0

    for i in number_list:
        if i == 1:
            number_of_solution += 1

    if(number_of_solution >= 2):
        total += 1

print(total)



    
    

    