# firstName = "John"
# lastName = "Smith"
# newPatient = True

# name = input("What is your name? ")
# print("Hello " + name)

# oopsies! error int - string
# birthYear = input("Enter your birth year: ")
# age = 2020 - birthYear
# print(age)

# better now
# birthYear = input("Enter your birth year: ")
# age = 2020 - int(birthYear)
# print(age)

# int() float() bool() str()

# firstNum = input("Enter your first number: ")
# secondNum = input("Enter your second number: ")
#
# sum = float(firstNum) + float(secondNum)
#
# print("Sum: " + str(sum))

# class Robot:
#     def introduceSelf(self):
#         print("My name is " + self.name) #self = this


class Robot:
    # using a constructor
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduceSelf(self):
        print("My name is " + self.name) #self = this


# r1 = Robot()
# r1.name = "Tom"
# r1.color = "red"
# r1.weight = 30
#
# r1.introduceSelf()
#
# r2 = Robot()
# r2.name = "Jerry"
# r2.color = "blue"
# r2.weight = 40
#
# r2.introduceSelf()
#

r1 = Robot("tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

# r1.introduceSelf()
# r2.introduceSelf()

class Person:
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting

    def sitDown(self):
        self.is_sitting = True

    def standUp(self):
        self.is_sitting = False

p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)

#p1 owns r2
p1.robotOwned = r2

#p2 owns r1
p2.robotOwned = r1

# p1.robotOwned.introduceSelf()

# print(type(True))

def c_greater_than_d_plus_e(c, d, e):
    return c > (d + e)

# print(c_greater_than_d_plus_e(10, 2, 20))

# a = [1, 3, 5, 7, 9, 11]
# #.append()
# b = []
# b.append(2)
# b.clear()
# print(b)

# c = []
# for x in a:
#     c.append(x * 2)
#
# # print(c)
#
# # same thing as above
# # list comprehension?
# d = [x * 2 for x in a]
# # print(d)
#
# e1 = []
# for x in range(1, 7):
#     e1.append(x ** 2)
#
# e2 = [x ** 2 for x in range(1, 7)]
# # print(e1)
# print(e2)
#
# #36, 25 16 9 4 1 ^ putting the above list in opposite order
# range(6, 0, -1) #range starts at 6, go to 0 but not including 0, and range goes "up" by -1
#
# f1 = []
# for x in range(6, 0, -1):
#     f1.append(x ** 2)
#
# f2 = [x ** 2 for x in range(6, 0, -1)]
#
# # print(f1)
# # print(f2)

# sets in python
# set is a type of data that stores a unique set of things
# {1, 3} <- 3
# {1, 3} duplicate element rejected

a = set()
# print(a) # set() printed out, represents empty set
#
a.add(1)
# print(a)
#
a.add(2)
# print(a)
#
a.add(2)
# print(a)

# iterate over every elem in set
# for x in a:
    # print(x)

# removing duplicates from a given list
given_list1 = [1, 1, 2, 4, 2]

new_set1 = set()
for x in given_list1:
    new_set1.add(x)
print(new_set1)

new_set1 = set(given_list1)
print(new_set1)

newList1 = []
for x in new_set1:
    newList1.append(x)

print(newList1)

newList1 = [new_set1]
print(newList1)

b = set()
b.add('apple')
b.add('banana')
b.add(1)
print(b)

# order of elems is different printed vs added?
# set doesn't store in order which things have been added, vs list which preserves order added

givenList2 = [1, 3, 4, 1, 3]
addSet = set(givenList2)
total = 0
for x in addSet:
    total += x
print(total)

total = sum(addSet)
print(total)