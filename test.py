# # class solution:
# #     def isPalindrome(self,x):
# #         if str(x) == str(x)[::-1]:
# #             return True
# #         else:
# #             return False

# # sol = solution()
# # Result = sol.isPalindrome(121)
# # print(Result)


# strs = ["flower","flow","flight"]

# class Solution:
#    def longestCommonPrefix(self, strs):
#     if not strs:
#       return ""
    
#     prefix = strs[0]
   
#     for s in strs[1:]:
#        while not s.startswith(prefix):
#          prefix = prefix[:-1]
#          if prefix == "":
#           return ""
#     return prefix
            

        
# Sol = Solution()
# Result = Sol.longestCommonPrefix(strs)
# print(Result)

# li = ['Harry','Sohan','Sachin','Rahul']
# for x in range(len(li)):
#     if li[x].startswith("S"):
#         print(f'{li[x]} welcome')

# n = int(input('Enter a number:'))
# i = 1
# while (i<11):
#     print(f'{n}x{i} = {n*i}')
#     i +=1 

# try:
#   n = int(input('Enter a number:'))
  
#   if n <= 0 :
#     print("Enter a positive number:")
    
#   else :
#     i = 1 
#     total = 0
    
#     while i <= n :
#       total += i 
#       i += 1 
      
#     print(total)
    
# except ValueError:
#   print('Enter a valid number')
# except EOFError:
#   print('No Input was provided')

# def Sum(n):
#     if (n == 1) :
#         return 1 
#     return Sum(n-1) + n 

# print(Sum(5))

# def pattern(n):
#     if (n == 0):
#         return
#     print("*" * n)
#     pattern(n-1)

# pattern(5)


# li = ['Anis','Rohan','an']

# def Remove(li,word):
#     n = []
    
#     for item in li :
#         n.append(item.strip(word))

#     for item in li :
#         li.remove(word)
#         return li
#     return n


# print(Remove(li,'an'))


