username = ""

if len(username) > 0 :
    print(f"welcome, {username}")
else:
    print ("error: username cannot be empty")


number = 10

if number > 10 :
     print("number is greater than 10")
elif number < 10 : 
     print("number is less than 10")
elif number == 10 :
     print("number is equal to 10") 
else:
     print("number is not a valid number")

x , y =5,10
print("yes") if x > y else print("no")