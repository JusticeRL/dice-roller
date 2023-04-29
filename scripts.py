import random

def getrolls(choice):
    rolls = input("How many would you like to roll? ")
    if rolls == "1":
        num1 = random.randint(1,int(choice))
        num2 = "Your roll is " + str(num1)
    else:
        for index in range(int(rolls)):
            if index == 0:
                num1 = random.randint(1,int(choice))
                num2 = "Your rolls are (" + str(num1) +", "
            elif 0<index<int(rolls)-1:
                num1 = random.randint(1,int(choice))
                num2 = num2 + str(num1) + ", "
            elif index == int(rolls)-1:
                num1 = random.randint(1,int(choice))
                num2 = num2 + "and " + str(num1) + ")"
            else:
                print("Something went wrong...")
    return num2

def getadv():
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    adv = input("Do you have advantage or disadvantage? ")
    if adv == "advantage":
        result = "Your rolls is " + str(max(num1,num2)) + " (" + str(num1) + "," + str(num2) + ")"
        return result
    elif adv == "disadvantage":
        result = "Your roll is " + str(min(num1,num2)) + " (" + str(num1) + "," + str(num2) + ")"
        return result
    elif adv == "no":
        result = "Your roll is " + str(num1)
        return 
    else:
        print("I dont understand that answe...")
        print()
        getadv()
