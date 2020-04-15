'''
    CS 5001
    Nathanial Ziegler
    April 2020
    Optional Lab
    Description:
        Part 3 responses
'''

from stack import Stack

def dictionary_sum(dictionary):
    total = 0
    for i in dictionary.values():
        total += i
    return total

def reverse_stack(old):
    new = Stack()
    while not old.is_empty():
        new.push(old.top())
        old.pop()
    return new
