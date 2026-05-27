# complement = ~13
# print(complement)

# And= 12 & 13
# print(And)

# OR = 12 | 13
# print(OR)

# XOR = 12 ^ 13
# print(XOR)

# LeftShift = 30 << 3
# print(LeftShift)

# RightShift = 30 >> 3
# print(RightShift)

# myList = ['a', 'b', 'c', 'd']
# print(myList[:3])
# # myList[2] = 'e'
# # print(myList)

# myList.append("e")
# print(myList)

# myList.insert(1, 'x')
# print(myList)

# thisList = (1,2,3,4,5) #tuple

# myList.extend(thisList)
# print(myList)

# del myList[3]
# print(myList)

# del myList 
# print(myList) #error because myList is deleted

# mylist = ['apple', 'banana', 'cherry']
# i = 0

# while i < len(mylist):
#     print(mylist[i])
#     i += 1

marks = [20,30,40,60]
new_marks = []

for x in marks:
    new_marks.append(x+2)

print(new_marks)

new_Marks = [x+2 for x in marks]
print(new_Marks)

Square = []

for x in range(0,11):
    if x % 2 == 0:
        Square.append(x ** 2)
        
print(Square)
        
square = [x ** 2 for x in range(10) if x % 2 == 0]
print(square)
