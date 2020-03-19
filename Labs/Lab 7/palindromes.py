'''
    Nathanial Ziegler
    CS 5001
    February 27, 2020
    Lab 7
'''

def is_pal(string):
    if len(string) == 0:
        return True
    else:
        if string[0] == string[-1]:
            return is_pal(string[1:-1])
        else:
            return False
