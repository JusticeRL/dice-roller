import scripts
import time

choice = 0
rolls = 0
adv = "no"

while True:
    output = 0
    choice = input("Which die would you like to roll? ")

    if choice == "exit":
        break
    
    try:
        temp = int(choice)
    except ValueError:
        print()
        print(".",end=" ")
        time.sleep(.5)
        print(".",end=" ")
        time.sleep(.5)
        print(".")
        time.sleep(.5)
        print()
        print("That is not a number, please try again.")
        print()
        continue

    if choice == "20":
        output = scripts.getadv()
    else:
        output = scripts.getrolls(choice)
    
    if output != 0:
       print()
       print(output)
       print()
