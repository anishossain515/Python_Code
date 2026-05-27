List1 = ['A','B','C','A','A','d']
ListA = []
ListB = []

for item in List1:
    if item == 'A':
        ListA.append(item)
    else:
        ListB.append(item)
print(ListA)
print(ListB)

#q1

def Find(n):
    if n % 2 == 0:
        print("even")
    else:
        print('odd')

Find(7)

#q2
s = "hello"
reversed_text = ""
for char in s :
    reversed_text = char + reversed_text
print(reversed_text)

#Q3
List2 = ['A', 'B', 'A', 'C', 'B', 'A']

count = {}

for item in List2:
    if item not in count:
        count[item] = 1
    else:
        count[item] +=1
print(count)

def fac(n):
    if n == 0 or n == 1 :
        return 1
    else:
        return n * fac(n-1)
    
print(fac(5))
