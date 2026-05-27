#1.Check if a year is a leap year 
year = int(input('Enter a year:'))
def check():
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
       print('Leap year')
    else:
        print('This year is not a Leap year')

check()

#2.Print numbers from 1 to 50 using a loop  
number_list = []

for x in range(1,51):
    number_list.append(x)

print(number_list)

#3. Print all even numbers between 1 and 100  
Even_numbers = [x for x in range(1,101) if x % 2 == 0]
print(Even_numbers)

#4.Find the sum of numbers from 1 to n  
n = int(input('Enter a range for how far you want to add: '))

result = 0

for x in range(n+1):
    result += x

print(result)

#5. Write a program to print multiplication table of a number  
N = int(input('Enter a range for how far you want to add: '))

for x in range(1,11):
    print(f'{N} x {x} = {N*x}')



#6.Find factorial of a number  
class Factorial:
    def __init__(self):
        self.n = int(input('Enter a number:'))

    def Fac(self,n):
        if n == 0 or n == 1:
           return 1
    
        return n * self.Fac((n) - 1)

f1 = Factorial()
print(f1.Fac(f1.n))

#7. Print Fibonacci sequence up to n terms 
n = int(input('Enter : '))
a,b=0,1
for i in range(n):
    print(a,end=' ')
    a , b = b, a+b
    
#8. Check if a number is prime  
n = int(input('Enter : '))
if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1)):
    print('This is a prime number')
else:
    print('This is not a prime number')

#9. Print all prime numbers between 1 and 100  
prime_numbers = []
for x in range(1,101):
    if x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1)):
        prime_numbers.append(x)

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

print(prime_numbers)

#10. Count digits in a number  
n = int(input('Enter : '))
Count = 0
for x in str(n):
    Count += 1

print(Count)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(2))