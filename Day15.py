numbers = [1,2,3,4,5,6,7,8,9,10]
total = 0

for num in numbers:
    total = total + num
# print(total)

#fibonacci sequence 
def fib(n):
    if n == 1 or n == 2 :
        return 1
    else :
        return fib(n-1) + fib(n-2)
print(fib(6))


def Fib(n):
    if n == 0:
        return 0
    elif n == 1 :
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
print(Fib(3))


for _ in range(2):
    print("Hi")


def creator():
    i = 1
    while i <= 200:
        yield i
        i +=1
x = creator()
print(next(x))
print(next(x))