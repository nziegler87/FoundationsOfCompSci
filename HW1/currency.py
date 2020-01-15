'''
    Nathanial Ziegler
    CS5001
    Homework 1
    January 15, 2020

    Description:
        This program displays the fee the user will pay to convert
        money from US Dollars to Wizarding Money. The user is prompted for
        a sum of money in USD and the conversion fee is displayed.

    Test Cases:
        * Input: $10, Conversion fee: $4.80
        * Input: $629, Conversion fee: $23.37
        * Input: $389, Conversion fee: $16.17
'''

# Flat conversion fee

CONVERSION_FEE = 4.50

def main():
    # Collects amount of money user wants to convert
    
    amount = float(input("Please enter an amount of money to convert.\n"))

    # Calculates fee user pays
    
    user_fee = amount * .03 + CONVERSION_FEE

    # Prints conversion fee to user
    
    print("Cheesy Joe's charges you ${:.2f}".format(user_fee))

main()
