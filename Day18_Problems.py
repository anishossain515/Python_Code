# numbers = [2,4,7,8,5]
# target = 9

# # for i in range(len(numbers)):
# #     for j in range(i + 1 , len(numbers)):
# #         if (numbers[i] + numbers[j]) == target :
# #             print(numbers[i],numbers[j])
       
# seen = {}

# for i in range(len(numbers)):
#     diff = target - numbers[i]
    
#     if diff in seen:
#         print(diff,numbers[i])
    
#     seen[numbers[i]] = i


#Basic Level 
#1. Write a program to input two numbers and print their sum
a = int(input('Enter first number : '))
b = int(input("Enter second number : "))
print(f"Their sum : {a + b}")

#2. Write a program to find the area of a rectangle  
Length = int(input('Enter your rectangle Length: '))
Width  = int(input('Enter your rectangle Width : '))
print(f"The area of Reactangle is {Length * Width }")

#3. Take a number as input and check if it is even or odd  
num = int(input("Enter a number: "))
if num % 2 == 0 :
    print('even')
else:
    print('odd')

#4. Write a program to swap two variables  
FirstVar = 5
SecondVar = 10
FirstVar , SecondVar = SecondVar , FirstVar
print(FirstVar)
print(SecondVar)

#5. Take a user's name and print a welcome message  
name = input('Enter your name:')
print(f"Welcome, {name}")

#6. Write a program to convert Celsius to Fahrenheit  
def celTFa(c):
    return ((c*9)/5)+32

print(celTFa(28))

#7. Take a number and print its square and cube  
def SqCu():
    n = int(input('Enter a number: '))
    print(n ** 2 , n ** 3)

SqCu()

#8. Write a program to check if a number is positive, negative, or zero  
Number = int(input("Enter a number: "))
if Number > 0 :
    print("positive")
elif Number < 0:
    print("negative")
else:
    print("zero")

#9. Take input of 3 numbers and print the largest  
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))

if x > y :
    if x > z:
        print(x)
    else:
        print(z)
elif y > z:
    print(y)
else:
    print(z)

#10. Write a program to calculate simple interest  
def interest():
    principal = int(input('Enter principle: '))
    rate = int(input('Enter rate as percentage: '))
    time = int(input('Enter time: '))
    print(principal * (rate/100) * time)
  
interest() 

    
