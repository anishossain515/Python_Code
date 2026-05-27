#problem
# numbers = [3,7,12,15,20]
# even_numbers = [x for x in numbers if x % 2 == 0]
# doubles = [x * 2 for x in even_numbers]

# for x in numbers:
#     if x % 2 == 0:
#         even_numbers.append(x)
#         doubles.append(x *2)
# print(even_numbers)
# print(doubles)

#problem-1
numbers1 = [5, 12, 7, 18, 3, 20, 11]
Even_numbers = [x for x in numbers1 if x % 2 == 0]
print(Even_numbers)

#problem-2
numbers2 = [4, 11, 7, 15, 2, 20]
Number = [x for x in numbers2 if x > 10]
squares = [x ** 2 for x in Number]
print(squares)

#problem-3
numbers3 = [-5, 3, -2, 8, 0, 7, -1]
Count = [x for x in numbers3 if x > 0]
print(len(Count))

#problem-4
numbers4 = [1, 4, 7, 10, 13, 6]
odd_numbers = [x for x in numbers4 if x % 2 != 0]
print(odd_numbers)
Sum = sum(odd_numbers)
print(Sum)

#problem-5
numbers5 = [45, 12, 78, 34, 89, 23]
numbers5.sort(reverse=True)
print(numbers5[0])
#Exceptionally
# numbers5.sort()
# print(numbers5[len(numbers5)-1])

# numbers5 = [45, 12, 78, 34, 89, 23]
# largest=numbers5[0]

# for x in numbers5:
#     if x > largest:
#        largest = x
             
# print(largest)

#problem-6
numbers6 = [10, 15, 20, 25, 30]
newNumber = []

for x in numbers6:
    if x % 2 == 0:
        newNumber.append(x * 2)
    if not x % 2 == 0:
        newNumber.append(x * 3)
print(newNumber)

# numbers = [45, 12, 78, 34, 89, 23]


# print("Largest:", largest)
# print("Index:", index)