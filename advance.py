from typing import List,Dict,Tuple,Union

# #using walrus operator
# if( n := len([1,2,3,4,5])) > 3:
#     print(f'List is too long {n} elements, expected <= 3')


# #types
# def Sum(a : int, b:int) -> int:
#     return a+ b

# value = Sum(3,4)
# print(value)

# #typing
# numbers : List[int] = [1,2,3,4]

# #match
# def https_status(status):
#     match status:
#         case 200:
#             return 'Ok'
#         case 404:
#             return 'Not Found'
#         case 500:
#             return 'Internal Server Error'
#         case _:
#             return 'Unknown status'
        
# print(https_status(404))


#exception handeling
# try:
#     a = int(input('Enter a number: '))
#     print(a)

# except Exception as e :
#     print(e)

# print('hi')


#try_except_else
#try:
  #somecode
#except:
   #somecode
#else:
  #code     #This is executed only if the try was successful


#try_except_finally
#try:
  #somecode
#except:
  #somecode
#finally:
  #code     #This is executed only if the try was successful

 
# print(__name__) #from where this code is executed __main__ or another file

#enumerate function
# l = [1,2,3,4]

# for index,item in enumerate(l):
#     print(f'The item number at index {index} is {item}') 


# n = int(input('Enter a number:'))

# table = [n*i for i in range(1,11)]
# with open('Tables.txt','a') as f:
#     f.write(f'Table of {n} : {str(table)} \n')


# name = input('Enter your name: ')
# marks = int(input('Enter your marks: '))
# phoneNumber = int(input('Enter your phone number: '))

# formatted_String = 'The name of student is {2},his marks are {0} and phone number is {1}'.format(marks,phoneNumber,name)
# print(formatted_String)

# table = [str(7*i) for i in range(1,11)]

# s = '\n'.join(table)
# print(s)

l = [2,5,10,45,42,25]

# def divisiable(n):
#      if (n%5 == 0):
#           return True
#      return False

# f = list(filter(divisiable,l))
# print(f)


# from functools import reduce
# def greater(a,b):
#     if(a>b):
#         return a
#     return b

# print(reduce(greater,l)) #at the first compare first two elements and then one by one
 