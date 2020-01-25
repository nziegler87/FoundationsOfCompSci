'''
    Nathanial Ziegler
    CS5001
    Homework 1
    January 15, 2020

    Description:
        User inputs minutes as float. Program calculates most possible
        years, days, minutes, hours, and seconds from the input.

    Test case #1:
    Input: 296.75
        Years: 0
        Days: 0
        Hours: 4
        Minutes: 56
        Seconds: 45

    Test case #2:
    Input: 42089.3
        Years: 0
        Days: 29
        Hours: 5
        Minutes: 29
        Seconds: 18

    Test case #3:
    Input: 600000
        Years: 1
        Days: 51
        Hours: 16
        Minutes: 0
        Seconds: 0
'''

# Time conversion constants used for program

MIN_IN_YEAR = 525600
MIN_IN_DAY = 1440
MIN_IN_HOUR = 60
MIN_IN_MIN = 1
SEC_IN_MIN = 60

def main():
    # Collects user minute input
    
    time_input = float(input("How many minutes are you measuring?\n"))

    # Calculates number of years and remaining time

    years = int(time_input // MIN_IN_YEAR)
    time_remaining = time_input % MIN_IN_YEAR

    # Calculates number of days and remaining time

    days = int(time_remaining // MIN_IN_DAY)
    time_remaining = time_input % MIN_IN_DAY

    # Calculates number of hours and remaining time

    hours = int(time_remaining // MIN_IN_HOUR)
    time_remaining = time_input % MIN_IN_HOUR

    # Calculates number of min and remaining time

    minutes = int(time_remaining // MIN_IN_MIN)
    time_remaining = time_input % MIN_IN_MIN

    # Calculates number of sec
    
    seconds = int(time_remaining * SEC_IN_MIN)

    # Prints breakdown of time

    print("That is...\n{} years\n{} days\n{} hours\n{} minutes, and"
          "\n{} seconds!".format(years, days, hours, minutes, seconds))

main()
