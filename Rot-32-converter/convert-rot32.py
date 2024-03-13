# a program to decrypt rot32.

def main():
    a = input("Enter the string: ")
    # shift = int(input("Enter the number: "))
    print(shiftString(a,32))

def shiftString(string, shift):
    result = ""
    for i in string:
        result += shiftChar(i, shift)
    return result

def shiftChar(char, shift):
    if char.isupper():
        return upperShift(char, shift)
    if char.islower():
        return lowerShift(char, shift)
    return char

def upperShift(char, shift):
    c = ord(char)
    c = (c + shift - 65) % 26 + 65
    return chr(c)

def lowerShift(char, shift):
    c = ord(char)
    c = (c + shift - 97) % 26 + 97
    return chr(c)

if __name__ == '__main__':
    main()
