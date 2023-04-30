import scripts
import time

choice = 0
rolls = 0
adv = "no"

while choice != "exit":
    output = 0
    
    choice = input("Which die would you like to roll? ")
    try:
        temp = int(choice)
    except ValueError:
        if choice == "exit":
            print()
            time.sleep(0.05)
            print("Goodbye.")
            print()
            time.sleep(0.05)
            continue
        else:
            print()
            print("...")
            time.sleep(.75)
            print("...")
            time.sleep(.75)
            print("...")
            time.sleep(.75)
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
    else:
        pass
    choice = input("Type 'exit' to quit. Otherwise, press enter: ").lower()
    print()
