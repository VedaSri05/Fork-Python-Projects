import random

x = "y"

while x == "y":

    # Generates a random number
    # between 1 and 6 (including
    # both 1 and 6)
    no = random.randint(1,6)

    if no == 1:
        print("[-----]")
        print("[ ]")
        print("[ 0 ]")
        print("[ ]")
        print("[-----]")
    if no == 2:
        print("[-----]")
        print("[ 0 ]")
        print("[ ]")
        print("[ 0 ]")
        print("[-----]")
    if no == 3:
        print("[-----]")
        print("[ ]")
        print("[0 0 0]")
        print("[ ]")
        print("[-----]")
    if no == 4:
        print("[-----]")
        print("[0 0]")
        print("[ ]")
        print("[0 0]")
        print("[-----]")
    if no == 5:
        print("[-----]")
        print("[0 0]")
        print("[ 0 ]")
        print("[0 0]")
        print("[-----]")
    if no == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[ ]")
        print("[0 0 0]")
        print("[-----]")

x=input("press y to roll again and n to exit:")
print("\n")

import random
while True:
    print('''1.roll the dice 2.To exit ''')
    user = int(input("what you want to do\n"))
    if user==1:
        number = random.randint(1,6)
        print(number)
    else:
        break