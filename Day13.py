def my_name(name):
    print("Hello " + name)
# my_name("Anis")

#to accept any number of positional arguments
def my_fun(greeting,*names):
    for name in names:
        print(greeting,name)

my_fun("Hello", "Anis","Onil","Ismail")


def my_cal(*numbers):
    total = 0
    for num in numbers:
        total +=num
    return total
print(my_cal(8,6,9))

#to accept any number of keyword arguments
def my_Fun(unsername , **details):
    print("username : " + unsername)
    print("Additional details :")
    for key,value in details.items():
        print(key + ":" + value)
my_Fun("anis515", age = "17", clg = "SCPSC", city = "Dhaka")

#to unpack positional arguments
def Sum(a,b,c):
    return a+b+c
numbers = [1,2,3]
result = Sum(*numbers)
print(result)

#to unpack keyword arguments
def det(name,email):
    print("Hello " + name , email)
person = {"name":"Anis","email":"anis@gmail.com"}
det(**person)

##
def display_info(dict):
    for key,value in dict.items():
        print(key + ":" + value)

details = {"name":"Anis", "age": "17"}
display_info(details)
    