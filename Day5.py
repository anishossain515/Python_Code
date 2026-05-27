myTuple = ("apple",)
print(type(myTuple))

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("banana")
y.insert(1,"ffa")
thistuple = tuple(y)
print(thistuple)

#set
mySet = {"apple","banana","cherry"}
mySet.add("orange")
print(mySet)
thiset = {1,2,3}
thiset.update(mySet)
print(thiset)