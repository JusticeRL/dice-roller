import random
import time

def getrolls(choice):
    while True:
        rolls = input("How many would you like to roll? ")
        if rolls == "exit":
            return "exit"
        try:
            rolls = int(rolls)
        except ValueError:
            time.sleep(0.1)
            print("That is not a number. Try again.")
            continue
        break

    if rolls == "1":
        num1 = random.randint(1,choice)
        num2 = "Your roll is " + str(num1)
    else:
        num2 = "Your rolls are ("
        for index in range(int(rolls)):
            if index<int(rolls)-1:
                num1 = random.randint(1,choice)
                num2 = num2 + str(num1) + ", "
            elif index == int(rolls)-1:
                num1 = random.randint(1,choice)
                num2 = num2 + "and " + str(num1) + ")"
    return num2

def getadv():
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    while True:
        adv = input("Do you have advantage or disadvantage? ")
        if adv == "exit":
            return "exit"
        elif adv == "advantage":
            return "Your rolls are " + str(max(num1,num2)) + " (" + str(num1) + "," + str(num2) + ")"
        elif adv == "disadvantage":
            return "Your rolls are " + str(min(num1,num2)) + " (" + str(num1) + "," + str(num2) + ")"
        elif adv == "no":
            return "Your roll is " + str(num1)
        else:
            print("I dont understand that answer...")
            print()
        
        