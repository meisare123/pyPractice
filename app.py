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

r1.introduceSelf()
r2.introduceSelf()

