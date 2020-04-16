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
    if int2 % int1 == 0:
        return True
    else:
        return False

def append(dictionary, key, value):
    if key not in dictionary.keys():
        dictionary[key] = value
    return dictionary

def more_efficient(string1, string2):
    efficiency_order = {"1":0, "lgn":1, "n":2, "nlgn":3, "nsquared":4}
    if efficiency_order[string1] < efficiency_order[string2]:
        return string1
    else:
        return string2

def stars(n):
    if not n:
        print("!!!")
    else:
        print("*")
        stars(n-1)
