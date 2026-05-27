thisDict = {
    "Name":"Anis",
    "clg": "SCPSC",
    "age" : 17
}

print(thisDict["clg"])

thisdict = dict(name = 'onil', age = 17)
print(thisdict.get("name"))

x = thisdict.keys()
print(x)

newDict = thisdict.copy()
newdict = dict(thisDict)

#nested dict
hisFamily = {
    "child1":{
        "name":"frin",
        "age": 12
    },

    "child2":{
        "name":"orfan",
        "age": 18
    }
}

print(hisFamily["child1"]["age"])