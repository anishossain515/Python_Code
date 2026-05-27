a = [6,3,1,8]
# a.sort()
# print(a)

# a.sort(reverse=True)
# print(a)

# a.reverse()
# print(a)


#how close the number is to 10
def myFun(n):
    return abs(n-10)

List = [22,2,45,32]
# List.sort(key=myFun)
# print(List)

# thisList = List.copy()
# print(thisList)

# thisList = list(List)
# print(thisList)

thisList = List[:]
# print(thisList)

#problem-1
numbers = [10,15,20,25,30]
# squares = [x **2 for x in numbers if x > 18]
squares = []
for i in numbers:
    if i > 18 :
        print(i)
        squares.append(i ** 2)
print(squares) 



