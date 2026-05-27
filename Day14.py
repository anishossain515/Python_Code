x = 200
def myfun():
    x = 300
myfun()
print(x)

y = 200

def myFun():
    global y 
    y = 300
myFun()
print(y)

def outer1():
    x = 100

    def inner1():
        x = 200
    inner1()
    return x
print(outer1())

def outer2():
    x = 300

    def inner2():
        nonlocal x
        x = 600
    inner2()
    return x
print(outer2())

#python decorators
def decorator(func):
    def wrapper():
        print("Transaction initiated")
        func()
        print("Transaction completed")
    return wrapper

# def hello():
#     print("...Executing all the steps of Transaction...")

# hello1 = decorator(hello)
# hello1()

@decorator
def hello():
    print("...Executing all the steps of Transaction...")

hello()

#map

marks = [77,97,68,49,66]

def grade(mark):
    if mark >= 80 :
        return "A+"
    elif 70 <= mark < 80 :
        return 'A'
    elif 60 <= mark < 70 :
        return "A-"
    else:
        return 'F'
Grades = list(map(grade,marks))
print("Students Marks:",marks)
print("Their Grade:",Grades)


def failing(mark):
    return mark < 60

result = list(filter(failing,marks))
print("Failure number:",result)


mark = [22,32,53,65,80]
odd = []

for x in mark:
    if x % 2 == 0 :
     odd.append(x)

print(odd)



# if __name__ == '__main__':
#     n = int(input().strip())
#     if n % 2 != 0 :
#          print("Weird")
#     elif 2 <= n <= 5:
#         print("Not Weird")
#     elif 6 <= n <= 20:
#         print("Weird")
#     elif x > 20:
#         print(" Not Weird")

# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a + b)
#     print(a - b)
#     print(a * b)

# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         print(i ** 2)

def is_leap(year):
    leap = False
    
    if year / 4 or year / 400 :
        leep = True
    elif year / 100 :
        leep = False
    
    return leap

year = int(input())
print(is_leap(year))