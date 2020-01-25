'''
    CS5003
    Lab 1
    Spring 2020
    Becker & Ziegler
'''

def main():
    print("Player Two, close your eyes!")
    secret_num = int(input("Player One: Choose a number between 2 and 10.\n"))
    print(35*"Scrolling to keep your number secret\n")
    secret_num2 = secret_num*2
    secret_num2 = secret_num2 + 5
    secret_num2 = secret_num2 * 50
    print("Player Two: enter the next set of info for Player One")
    magic_offset = int(input("Enter 1770 if P1's nirthday ALREADY passed. Otherwise enter 1769\n"))
    secret_num2 = secret_num2 + magic_offset
    birthday = int(input("What year was Player One born?\n"))
    secret_num2 = secret_num2 - birthday
    print("The secret number and age is",secret_num2)
main()
