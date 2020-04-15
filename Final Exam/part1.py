'''
    Nathanial Ziegler
    CS 5001
    Final Exam
    April 15, 2020
    Description:
        part1.py

    I pledge on my honor that I did not give or receive help on this exam.
'''

def divides(int1, int2):
    pass


def append(dictionary, key, value):
    if key in dictionary.keys():
        return dictionary
    else:
        dictionary[key] = value
        return dictionary

def more_efficient(string1, string2):
    efficiency_order = {"1":1, "lgn":2, "n":3, "nlgn":4, "nsquared":5}
    
