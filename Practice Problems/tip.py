'''
    CS5001
    Spring 2020
    Practice Problem 2

    Test Case:


'''

def main():
    check_amount = float(input("What was your check amount?\n"))
    tip_amount = float(input("What percentage would you like to tip?\n"))
    tip = check_amount * (tip_amount / 100)
    print("For a {}% tip, you should leave your sever ${:.2f}.".format(tip_amount , tip))

main()
