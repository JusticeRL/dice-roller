import random

num1 = 0
num2 = 0
output = 0
choice = 0
rolls = 0
adv = "no"

while choice != "exit" and choice != "Exit":
    choice = input("Which die would you like to roll? ")

    if choice == "20":
        num1 = random.randint(1,20)
        num2 = random.randint(1,20)
        adv = input("Do you have advantage? ")
        if adv == "yes" or adv == "Yes":
            output = "You rolled a (" + str(num1) + " and a " + str(num2) +"). Leaving you with " + str(max(num1,num2))
        else:
            adv = input("Do you have disadvantage? ")
            if adv == "yes" or adv == "Yes":
                output = "You rolled a (" + str(num1) + " and a " + str(num2) +"). Leaving you with " + str(min(num1,num2))
            else:
                output = "You rolled a " + str(num1)
    else:
        rolls = input("How many dice would you like to roll? ")
        i = 0
        while i < int(rolls):
            num1 = random.randint(1,int(choice))
            if i == 0:
                num2 = str(num1) + ", "
            elif i < (int(rolls)-1):
                num2 = num2 + str(num1) + ", "
            else:
                num2 = num2 + "and " +str(num1)
            i += 1
        output = "Your rolls are (" + num2 + ")"

    print(output)
    choice = input("If you want to roll again, press enter. Otherwise, type 'exit' ")
