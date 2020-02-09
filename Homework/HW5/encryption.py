'''
    Nathanial Ziegler
    CS 5001
    INSERT DATE
    HW 5
    Description:
        UPDATE
    Referenced:
        https://www.geeksforgeeks.org/string-punctuation-in-python/
        https://stackoverflow.com/questions/16060899/alphabet-range-in-python
'''

import string
EXCLUDE = list(string.digits + string.punctuation + string.whitespace)

def encrypt(message, shift):
    ''' Name: encrypt
        Inputs: message (str), shift amount (int)
        Returns: encrypted message (str)
    '''
    shift = check_max_shift(shift)
    message = message.lower()
    unencrypted_list = list(message)
    encrypted_list = []
    
    for i in range(len(unencrypted_list)):
        if unencrypted_list[i] in EXCLUDE:
            encrypted_list.append(ord(unencrypted_list[i]))
        else:
            unencrypted_val = ord(unencrypted_list[i])
            encrypted_val = unencrypted_val + shift
            if encrypted_val > ord('z'):
                remainder = encrypted_val % ord('z')
                encrypted_val = remainder + ord('a') - 1
            encrypted_list.append(encrypted_val)
    encrypted_string = ""
    for i in range(len(encrypted_list)):
        encrypted_string += chr(encrypted_list[i])
    return encrypted_string

def decrypt(message, shift):
    ''' Name: decypt
        Inputs: message (str), shift amount (int)
        Returns: decrypted message (str)
    '''
    shift = check_max_shift(shift)
    message = message.lower()
    encrypted_list = list(message)
    decrypted_list = []

    for i in range(len(encrypted_list)):
        if encrypted_list[i] in EXCLUDE:
            decrypted_list.append(ord(encrypted_list[i]))
        else:
            encrypted_val = ord(encrypted_list[i])
            decrypted_val = encrypted_val - shift
            if decrypted_val < ord('a'):
                remainder = ord("a") % decrypted_val
                decrypted_val = ord("z") - remainder + 1
            decrypted_list.append(decrypted_val)
    decrypted_string = ""
    for i in range(len(decrypted_list)):
        decrypted_string += chr(decrypted_list[i])
    return decrypted_string
                

def check_max_shift(shift):
    ''' Name: check_max_shift
        Input: shift (int)
        Renturns: shift value as int unless over 25 then shift value of 1
    '''
    if shift > 25:
        shift = 1
    return shift

def convert_to_ascii(char_list):
    ''' Name: convert_to_ascii
        Input: list of characters (strings)
        Returns: list of characters, each converted to ascii values (ints)
    '''
    ascii_list = []
    for i in range(len(char_list)):
        value = ord(char_list[i])
        ascii_list.append(value)
    return ascii_list
