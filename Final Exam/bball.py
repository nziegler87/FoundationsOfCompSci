'''
    Nathanial Ziegler
    CS 5001
    Final Exam
    April 15, 2020
    Description:
        bball.py

    I pledge on my honor that I did not give or receive help on this exam.
'''

class BBallPlayer:
    def __init__(self, name, inches):
        self.name = name
        self.height = inches

    def same(self, other):
        return self.height == other.height
