import random

print('Hello, World!')

if 5 > 3:
   print('Five is greater than three!')
   x=5 
   print(x) 

if 5 > 2:
   print('Five is greater than two!')
   y=5 
   print(y)

print("Hi");print("welcome to python programming", end="...")

"""
this is multiline string
"""
A_5 = 54
print("A_5",A_5)

x,y,z=1,2,3
print(y)

x=y=z=10
print(x,y,z)

fruits = ["apple", "banana", "cherry"]
x,y,z=fruits
print(x)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

X=50 #global variable

def myNumber():
    y=60 #local variable
    print(y+X)
myNumber()

def myNum():
    global num
    num = 110
myNum()

print(num)

x = str(3)
print(type(x))

print(random.randrange(1,10))