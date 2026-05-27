# class Employee:
#     language = 'py' #this is a class attribute
#     salary = 1200000

#     def __init__(self): #dunder method which is automatically called
#         pass

# ismail = Employee()
# ismail.name = 'Ismail'#this is a instance attribute

# print(ismail.name,ismail.language, ismail.salary)



# class Programmers:
#     company = 'Microsoft'
#     def __init__(self,name,salary,pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin

#     def __str__(self):
#         return f'Name : {self.name}, Salary : {self.salary}, Pin : {self.pin}'

# p1 = Programmers('Anis',1200000,235234)

# print(p1)

# list1 = []

# for x in p1.__dict__.values():
#     list1.append(x)

# print(list1)



# class Calculator:
#     def __init__(self,number):
#         self.number = number

#     def square(self):
#         return self.number ** 2
    
#     def cube(self):
#         return self.number ** 3
    
#     def sqareRoot(self):
#         return int(self.number ** (0.5))
    
#     @staticmethod
#     def greet():
#         print('Hello')
     
# Count = Calculator(16)
# print(Count.sqareRoot())
# Count.greet()
 
#iteration
# class EvenNumber:
#     def __iter__(self):
#         self.x = 2
#         return self
    
#     def __next__(self):
#         n = self.x
#         self.x +=2
#         return n
    
# even = EvenNumber()
# it = iter(even)

# print(next(it))
# print(it.__next__())




# class TwoDVector:
#     def __init__(self,i,j):
#         self.i = i
#         self.j = j

#     def show(self):
#         print(f'The vector is {self.i}i + {self.j}j')


# class ThreeDVector(TwoDVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k = k

#     def show(self):
#         print(f'The vector is {self.i}i + {self.j}j + {self.k}k')
        
# a = TwoDVector(1,2)
# a.show()

# b = ThreeDVector(1,2,3)
# b.show()


# class Employee:
#     salary = 234
#     increment = 0.2

#     @property
#     def salayAfterIncrement(self):
#         return self.salary + self.salary * self.increment

# e = Employee()

# print(e.salayAfterIncrement)

