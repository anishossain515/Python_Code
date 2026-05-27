#problem 1 
data = [23, -5, 45, None, 12, -9, 30, None, 18]
newData = [x for x in data if x is not None and x >= 0]
print(newData)

#in another way
# for x in data:
#     if x is None:
#         continue
#     elif x < 0 :
#         continue
#     newData.append(x)

# print(newData)

#problem 2
prices = [1200, 1500, 800, 2000, 950]
NewPrices = [x / 1000 for x in prices]
print(NewPrices)

#problem 3
labels = ["cat","dog","cat","cat","dog","bird","dog","cat","horse","horse"]
# Cat = labels.count("cat")
# Dog = labels.count("dog")
# Bird = labels.count("bird")

# Dict = dict(cat = Cat , dog = Dog , bird = Bird)

# print(Dict)


#best way for problem 3
Dict = {}

for label in labels:
    if label not in Dict:
         Dict[label] = 1
    else:
        Dict[label] += 1    

print(Dict)
#problem 4
predictions = [1,0,1,1,0,1,0,0,1,1]


# one = predictions.count(1)
# zero = predictions.count(0)

# if one > zero:
#     print(1)
# else:
#     print(0)

#best way for problem 4
counts = {}

for p in predictions:
    counts[p] = counts.get(p, 0) + 1

majority = max(counts, key=counts.get)
print(majority)

#problem 5
ratings = {
    "Alice":5,
    "Bob":3,
    "Charlie":4,
    "David":2,
    "Eva":5
}

recommanded = []

for name , rating in ratings.items():
    if rating >= 4:
        recommanded.append(name)
print(recommanded)