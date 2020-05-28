'''
    Nathanial Ziegler
    CS 5001
    Final Exam
    April 15, 2020
    Description:
        part2.py

    I pledge on my honor that I did not give or receive help on this exam.
'''

from stack import Stack
from bball import BBallPlayer

def equal_stacks(stack1, stack2):
    while not stack1.is_empty():
        if stack2.is_empty():
            return False
        
        if stack1.top().same(stack2.top()):
            stack1.pop()
            stack2.pop()
        else:
            return False

    if stack1.is_empty() and stack2.is_empty():
        return True
    else:
        return False
