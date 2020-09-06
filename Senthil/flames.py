mapPrintvalues = {
    'f': "friends",
    'l': "lovers",
    'a': "affectionate",
    'm': "married",
    'e': "enemies",
    's': "Siblings"
}


def getRelationshipByFlamesFor(person1, person2):
    if person1 == person2:
        return "Invalid input- Both inputs are same"
    elif (isinstance(person1, str) and isinstance(person2, str)) is False:
        return "Invalid input- Need valid string input"
    elif person1 == "" or person2 == "":
        return "One or both inputs are blank"
    else:
        person1 = "".join(person1.split(" "))
        person2 = "".join(person2.split(" "))
        opPerson = person2
        commonCount = 0
        for i in range(len(person1)):
            index = person2.find(person1[i])
            if index >= 0:
                commonCount += 1
                person2 = person2[0:index] + person2[index + 1:]
                #print(person2)
        count = len(person1) + len(person2) - commonCount
        #print("count=", count)
        return person1 + " and " + opPerson + " are meant to be " + getrelationshipByCount(count - 1)


def getrelationshipByCount(count):
    flamesList = list(mapPrintvalues.keys())
    index = 0
    while len(flamesList) > 1:
        for i in range(count):
            index += 1
            if index > (len(flamesList) - 1):
                index = 0
        #print("remove=", flamesList[index], "index= ",index)
        flamesList.remove(flamesList[index])
        if index > (len(flamesList) - 1):
            index = 0
        #print(flamesList)

    return mapPrintvalues[flamesList[0]]


# test= "oop"
# ip = "o"
# test = test[0:test.find(ip)] + test[test.find(ip)+1:]
# test = test[0:test.find(ip)] + test[test.find(ip)+1:]
# ip = "p"
# test = test[0:test.find(ip)] + test[test.find(ip)+1:]
# print(test)
# print(getRelationshipByFlamesFor("a", "b"))
# print(getrelationshipByCount(11))
# flamesList = ['f', 'l', 'a', 'm', 'e', 's']
# flamesList.remove(flamesList[1])
# print(flamesList)
# print(mapPrintvalues.keys())

print(getRelationshipByFlamesFor("vign esh", "poornima"))
print(getRelationshipByFlamesFor(" vignesh ", "po o rn im a"))
# print(getRelationshipByFlamesFor("vignesh", "poornima                 "))
# print(getRelationshipByFlamesFor("dnukuma", "mukund"))


