# new file which to store the 6 python exercises on

def sleepIn(weekday, vacation):
    # if its not weekday OR if its a vacation day, sleep in
    # if it is a weekday and not a vacation day, dont sleep in :'(
    return ((not weekday) or vacation)


def stringTimes(text, times):
    # WAAAYY SIMPLER SOLUTION: return text * times
    newString = ''
    for x in range(0, times):
        newString += str
    return newString


# print("hi" * 4)

def sayHello(name):
    return "Hello " + name + "!"


def firstLast6(givenList):
    # (givenList[givenList.len - 1] == 6) <- was my first attempt
    # list[-1] returns the last element in the list
    if (givenList[0] == 6) or (givenList[-1] == 6):
        return True
    return False

def doubleChar(givenString):
    # not my solution, testing out + for strings
    newString = ''
    for i in givenString:
        newString += i * 2
    return newString

def countEven(numList):
    total = 0
    for i in numList:
        if (i % 2 == 0):
            total += 1
    return total