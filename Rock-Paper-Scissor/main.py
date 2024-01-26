from random import randint

def main(me = 0, robot = 0):
    a = 0
    while(1):
        print(f"Score:\nYou: {me}\nRobot: {robot}\n")
        print("1: Rock\n2: Paper\n3: Scissor\n4: Exit")
        try:
            a = int(input("Enter Your Choice: "))
            if a == 4:
                printWinner(me,robot)
                return
            elif a > 4 or a < 1:
                print("Invalid Input\n");
                main(me, robot)
                return
        except:
            print("Invalid Input\n");
            main(me, robot)
            return
        b = randint(1,3)
        c = winner(a,b)
        print(f"The Robot: {b}\n")
        if(c == 1):
            me+=1
        elif c == 2:
            robot+=1
        else:
            print("Draw.\n")

def winner(x,y):
    #1 is rock, 2 is paper, 3 is scissor.
    if x == y:
        return 0
    if x == 1:
        if y == 3:
            return 1
        return 2
    elif x == 2:
        if y == 3:
            return 2
        return 1
    elif x == 3:
        if y == 1:
            return 1
        return 2
    else:
        print("Invalid Parameters.\n")
        return

def printWinner(me, robot):
    print(f"Score:\nYou: {me}\nRobot: {robot}\n")
    if me < robot:
        print(f"Robot Won by {robot-me} points.")
    elif me > robot:
        print(f"You Won by {me-robot} points.")
    else:
        print("Both of you have same Point.\nDraw Game.")


if __name__ == '__main__':
    main()