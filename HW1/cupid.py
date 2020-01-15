'''
    Nathanial Ziegler
    CS5001
    Homework 1
    January 15, 2020

    Description:
        This program prompts the user to input stats and then displays
        them on the screen.
'''

def main():

    # Collects user stats
    
    first_name = input("Enter your first name.\n")
    last_name = input("Enter your last name.\n")
    age = int(input("Enter your age in years.\n"))
    income = float(input("Enter your average annual income.\n"))
    dogs = int(input("Enter the number of dogs in your family.\n"))
    twilight = input("Team Jacob or Team Edward?\n")

    # Prints stats, each on one line
    
    print("\nThank you for your profile information! Here's what we stored "
          "for you.\n\nName:", first_name, last_name, "\nAge:", age,
          "\nIncome: ${:.2f}".format(income), "\nYou have", dogs,
          "dog(s)", "\nYou are on team", twilight)


main()
