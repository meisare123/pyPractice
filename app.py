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

a = [1, 3, 5, 7, 9, 11]
#.append()
b = []
b.append(2)
b.clear()
# print(b)

c = []
for x in a:
    c.append(x * 2)

print(c)

# same thing as above
d = [x * 2 for x in a]
print(d)

e1 = []