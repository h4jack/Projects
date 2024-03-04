from art import tprint
from time import sleep
from os import system

def main():
    try:
        a = int(input("Enter the time in second: "))
    except:
        print("invalid input: ")
        main()
    printTime(a)

def printTime(a):
    while(a != 0):
        system("cls")
        tprint(str(a), "random")
        a-=1
        sleep(1)
    system("cls")
    tprint(str(a), "random")
    tprint("time up..")

if __name__ == '__main__':
    main()
    