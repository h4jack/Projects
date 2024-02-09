#create a number guessing game from both side user and robot.

from random import randint as rint

#variables
rmax = 0
op = 1


def main():
    print("who is going to guess.\n1. Me(Robot), \n2. You(User): ")
    op = takeInput("Enter the number: ",1,2)
    if(op == 1):
        guessRobot()
    elif(op == 2):
        guessUser()
    op = input("do you want to play again (y/n): ")
    if(op == 'y'):
        main()
    print("Oops.. Game Terminated.")



def inputError(c = ""):
    print("Wrong Input.\n",c);

def takeInput(str, min = -1, max = -1):
    t = True
    while(t):
        try:
            a = int(input(str))
            if(min != max):
                if(a >= min and a <= max):
                    t = False
                else:
                    inputError(f"Enter a number between {min} and {max}.")
            else:
                t = False
        except:
            inputError("Enter a valid numbers.")
    return a

def guessRobot():
    x = rint(1,4);
    rlim = (100**x)
    a = takeInput(f"now think of a number between 1 to {rlim}: ",1,rlim)
    guesstime = 0;
    rmin = 1
    rmax = rlim
    print("Enter 0: if number is currect.")
    print("Enter 1: if number is less then.")
    print("Enter 2: if number is greater.")
    while(1):
        guesstime += 1
        num = rint(rmin,rmax)
        print(f"I think you guessed the number {num}")
        op = takeInput("Am i right (0/ 1/ 2): ",0,2)
        if(op == 0):
            print(f"the number is {a}. this guessing took me {guesstime} times")
            break
        elif(op == 1):
            rmin = num
        elif(op == 2):
            rmax = num
    op = input("do you want to play again (y/n): ")
    if(op == 'y'):
        guessRobot()
    print("exit from Robot Guessing game.")
        

def guessUser():
    print("1:  (Easy)   1-100")
    print("2:  (Normal) 1-10,000")
    print("3:  (Midium) 1-1,000,000")
    print("4:  (Hard)   1-100,000,000")
    op = takeInput("Select Your Difficulty Level: ", 1, 4)
    rlim = (100**op)

    guessnum = rint(1,rlim)
    guesstime = 0;

    while(1):
        guesstime += 1
        op = takeInput("Now Guess the number: ", 0, rlim)
        if(op == guessnum):
            print(f"you are currect. Your guessing took you {guesstime} times")
            break
        elif(op == 0):
            print(f"the number is {guessnum}\n This took you {guesstime} times but still you failed.")
            break
        elif(op > guessnum):
            print(f"The number is less then {op}")
        elif(op < guessnum):
            print(f"The number is greater then {op}")
        print("Guess Again or exit(0):")
    op = input("do you want to play again (y/n): ")
    if(op == 'y'):
        guessUser()
    print("exit from User Guessing game.")

if __name__ == '__main__':
    main()