from array import *

Arr = array('i',[])

n = int(input("How many values you want to add:"))

for i in range(0,n):
    Arr.append(int(input("Enter next value: ")))

for x in Arr:
    print(x, end=" ")

print("\n")

firstValue = Arr[0]
NewArr = array('i',[])

# for x in Arr:
#     if firstValue < x:
#         firstValue = x
#         NewArr.append(firstValue)
#     else:
#         continue

# for x in NewArr:
#     print(x, end = " ")

print("\n")

#alternative way
for i in range(len(Arr)):
    for j in range(i + 1, len(Arr)):
        if Arr[i] > Arr[j]:
            Arr[i], Arr[j] = Arr[j], Arr[i]
            NewArr.append(Arr[i])

