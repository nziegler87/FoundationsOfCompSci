'''
    CS5001
    Spring 2020
    Source code from class - myNEU
'''

import random

def randomize_tuition():
    ''' Function: randomize_tuition
        Parameters: none
        Returns: floats, the amount of tuition this year
    '''
    tuition = random.randint(8000, 12000)
    return tuition

def calculate_tuition_v2(pct_scholarship):
    ''' Function: calculate_tuition_v2
        Parameters: pct of scolarship we got (0-1) float
        Returns: amount left to pay (float)
    '''
    tuition = randomize_tuition()
    left_to_pay = tuition - pct_scholarship * tuition
    return left_to_pay


def calculate_tuition(tuition, pct_scholarship):
    ''' Function: calculate_tuition
        Parameters: tuition, pct scholarship (floats)
        Return: amount left to pay (float)
    '''
    left_to_pay = tuition - pct_scholarship * tuition
    return left_to_pay

def main():
    to_pay = calculate_tuition(12000, .5)
    print("You still have to pay $", round(to_pay, 2), sep = "")

    tuition = float(input("How much is tuition?\n"))
    scholarship = float(input("How much is FB covering? (0-1)?\n"))
    to_pay = calculate_tuition(tuition, scholarship)
    print("NOW you still have to pay $", round(to_pay, 2), sep = "")
 
main()
