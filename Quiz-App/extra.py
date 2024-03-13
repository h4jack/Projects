import sys

def takeInt(prompt="", min_val=0, max_val=0):
    try:
        min_val, max_val = int(min_val), int(max_val)
    except ValueError:
        raise ValueError("Invalid arguments for input range.")

    if min_val > max_val:
        print("Invalid argument for the range")
        sys.exit()

    while True:
        try:
            user_input = input(prompt)
            if user_input.lower() == 'q':
                print("Exiting the program.")
                sys.exit()
            num = int(user_input)
            if (min_val <= num <= max_val) or (min_val == max_val):
                return num
            else:
                print(f"Please enter a number in the range {min_val} to {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")