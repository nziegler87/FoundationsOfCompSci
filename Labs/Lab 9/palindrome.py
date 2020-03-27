from stack import Stack

PALS = ['tacocat', 'radar', 'borroworrob', 'madamimadam', 'aa', 'a', '']

def is_pal2(string):
    ''' Name: is_pal2
        Parameters: a string to be tested if palidrome
        Returns: a boolean indicating if the string is a palindrome
    '''
    char_reversed = Stack()

    for character in string:
        char_reversed.push(character)

    for character in string:
        if character != char_reversed.top():
            return False
        else:
            char_reversed.pop()

    return True

