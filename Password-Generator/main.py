#a program to generate passowrd.

from random import randint as rint

special_char = "!\"#$%&'()*+,-./:;<=>?@[\\]^_{|}~` "
upper_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_char = "abcdefghijklmnopqrstuvwxyz"
num_char = "0123456789"

def main(c):
    a = 8
    match(c):
        case "1":
            pass
        case "2":
            try:
                a = int(input("Enter the length of the password : "))
            except:
                print("invalid input generating rendom password.")
        case _:
            return
    print("The generated password is : ", generate_password(a))
    print("1. if you want to generate again with the same length.")
    print("2. if you want to generate again with a new length.")
    print("or exit...")
    main(input("Enter : "))

def generate_password(a):
    slen = len(special_char)
    ulen = len(upper_char)
    llen = len(lower_char)
    nlen = len(num_char)

    password = ""

    for _ in range(a):
        c = rint(0,3)
        match(c):
            case 0:
                password += special_char[rint(0,slen-1)]
            case 1:
                password += upper_char[rint(0,ulen-1)]
            case 2:
                password += lower_char[rint(0,llen-1)]
            case 3:
                password += num_char[rint(0,nlen-1)]
    return password



if __name__ == '__main__':
    main("2")
    print("Program Terminated...")