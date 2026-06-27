###1

'''
height = float(input("Please enter your height: "))
if(height >= 140):
    print("Welcome to the roller coaster!")
else:
    print("sorry, you're too short ")
'''

###2

'''
priceCredit = float(input("Enter full ticket price: "))
isStudent = (input("Are you a student? (True/False):"))

if(isStudent == "True"):
    priceCredit = priceCredit * 0.8
    print("price after discount: " , priceCredit)
else:
    print("Full price", priceCredit) 
'''

###3

'''
cpuTemp = float(input("Enter CPU temperature: "))
if cpuTemp > 85:
    print("Warning: CPU too hot!")
else:
    print("Temperature is normal.")
'''

###4

'''
answerCorrect = int(input("Enter the number of correct answers (0-30): "))
if answerCorrect >= 26:
    print("You passed the exam!")
else:
    print("You failed, try again next week.")
'''

###5

'''
ticketType = input("Which ticket type do you have: ")
pointsCount = int(input("How many points do you have? "))
if ticketType == "Economy Plus" and pointsCount > 5000:
    print("You are eligible for an upgrade ")
else:
    print("You are not eligible for an upgrade.")
'''

###6
'''
playerCount = int(input("How many players are connected? "))
if playerCount == 1000:
    print("The server is full")
elif playerCount > 950:
    print("The server is almost full")
else:
    print("There is room on the server") 
'''

###7

'''
coffeeCount = int(input("How many cups of coffee did you buy? "))
if coffeeCount < 10:
    print("bronza")
elif coffeeCount <= 25:
    print("silver")
else:
    print("gold")
'''

###8

'''
vehicleSpeed = int(input("what is the speed of the vehicle: "))
if vehicleSpeed <= 90:
    print("correct speed")
elif vehicleSpeed <= 110:
    print("Warning!")
else:
    print("heavy fine")
'''
###9

'''
firstCode = int(input("Enter code: "))
if firstCode == 1234:
    print("The safe was opened")
else:
    backupCode = int(input("Enter code: "))
    if backupCode == 9999:
        print("The safe was opened using a backup code")

    else:
        print("The alarm was activated")
'''
###10

'''
amountMeal = float(input("The amount of the meal: "))
satisfaction = int(input("What is the level of satisfaction: (1-3) "))
if satisfaction == 1:
    amountMeal = amountMeal * 0.1
    print("The sum of tip = ", amountMeal )
elif satisfaction == 2:
    amountMeal = amountMeal *0.15
    print("The sum of tip = ", amountMeal )
else:
    amountMeal = amountMeal * 0.22
    print("The sum of tip = ", amountMeal )
'''

###11

'''
weight = float(input("What is weight for an apple? "))
color = input("What is color: ")
if (150 <= weight <= 250) and (color == "green" or color == "red"):
    print("apple for export")
else:
    print("Apple for the local market")
'''

###12

'''
number1 = int(input("What is number1: "))
number2 = int(input("What is number2: "))
number3 = int(input("What is number3: "))

if ((number1 + number2 > number3) and
    (number1 + number3 > number2) and
    (number2 + number3 > number3)):
    print("They can!")
else:
    print("They can't")
'''

###13

'''
batteryPercent = int(input("battery Percentage: "))
windSpeed = int(input("wind speed: "))
isCritic = input("Is it a critical mission? (True\False)")
isCritic = (isCritic == "True")

if isCritic:
     if batteryPercent == 0:
          print("Emergency landing")
     else:
          print("continue to flight")
          
else:
    if batteryPercent < 15 or windSpeed > 40:
         print("Emergency landing")
    else:
        print("continue to flight") 

'''

###14

'''
salary = int(input("salary: "))
tax = salary * 0.1
if salary <= 5000:
    print("Tax = ", tax)
else:
    tax = 5000*0.1 + ((salary - 5000) *0.2)
    print("Tax = ", tax)

'''

###15

year = int(input("Enter year: "))
if year % 4 == 0:
    if year % 100 != 0:
        print("yes")
    elif year % 400 == 0:
        print("yes")
    else:
        print("No")
else:
    print("No")
