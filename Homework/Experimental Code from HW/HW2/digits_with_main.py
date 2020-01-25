'''
    Nathanial Ziegler
    CS5001
    Homework 2
    January 21, 2020
    Description:
        For this program, the user inputs an integer number and then
        the a value to isolate a number in the 10^n place.
    Consulted: https://www.geeksforgeeks.org/abs-in-python/
'''

def get_digit(num, power):
    ''' Function: get_digits
        Inputs: Number (int) and 10^n digit to isolate from number (int)
        Returns: Isolated number of 10^n input as int
        Does: Isolates 10^n digit from inputed integer and n values
    '''
    abs_num = abs(num)
    isolated_num = abs_num // 10**power
    isolated_num = isolated_num % 10
    return isolated_num

def main():
    # Collect starting values from user
    num = int(input("Enter number integer number: "))
    power = int(input("Enger the 10^n you want to isolate: "))

    # Calculate isolated value
    isolated_val = get_digit(num, power)

    # Print isolated value
    print(isolated_val)

main()
