import random
from scripts import *


output = 0
choice = 0
rolls = 0
adv = "no"

while choice != "exit" and choice != "Exit":
    choice = input("Which die would you like to roll? ")

    if choice == "20":
        output = getadv()
    else:
        output = getrolls(choice)
    
    print()
    print(output)
    print()
    choice = input("Type 'exit' to quit. Otherwise, press enter: ")
    print()
