import numpy as np
import os

electricity_units = np.array([
    [55, 65, 75],
    [120, 150, 170],
    [210, 230, 240]
])


def costSlab1(units):
    print("Bill for S1 lab is")
    for value in units:
        value *= 10
        print(value, end="\t\t")
    print("\n")


def costSlab2(units):
    print("Bill for S2 lab is")
    for value in units:
        value *= 15
        print(value, end="\t")
    print("\n")


def costSlab3(units):
    print("Bill for S3 lab is")
    for value in units:
        value *= 30
        print(value, end="\t")
    print("\n")


menu = True
while menu:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\tWELCOME TO BILL CALCULATING SYSTEM")
    print("My student id is 23Y390001")
    print("Enter your choice")
    print("Press 1 to display the bill of slab1 and slab 2.")
    print("Press 2 to display the bill of slab3.")
    print("Press any other key to exit.")
    choice = int(input("Your choice: "))
    if choice == 1:
        costSlab1(electricity_units[0])
        costSlab2(electricity_units[1])
        input("press any continue using system")
    elif choice == 2:
        costSlab3(electricity_units[2])
        input("press any continue using system")
    else:
        menu = False
