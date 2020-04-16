'''
    Nathanial Ziegler
    CS 5001
    Final Exam
    April 15, 2020
    Description:
        part3.py

    I pledge on my honor that I did not give or receive help on this exam.
'''

def all_there(nested, n,  m):
    count = n * m
    combined = []
    for i in range(n):
        for j in range(m):
            combined.append(nested[i][j])
    
    value = 0
    for i in range(count):
        if value in combined:
            combined.remove(value)
        value += 1

    if not combined:
        return True
    else:
        return False

def is_missing(lst):
    '''
    Runtime complexity = O(n)
    '''
    minimum = lst[0]
    for item in lst:
        if item < minimum:
            minimum = item

    length = len(lst) + 1

    for i in range(length):
        if minimum not in lst:
            return minimum
        else:
            minimum += 1
