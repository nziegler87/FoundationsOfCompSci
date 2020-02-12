'''
    Nathanial Ziegler
    CS 5001
    February 12, 2020
    HW 5
    Description:
        Functions to encrypt and decrypt messages. Both work by
        converting each character in a string to an ascii value, applying
        designated shift (excluding spaces and punctuation), and then converting
        ascii values back to characters.

    Referenced:
    https://www.geeksforgeeks.org/string-punctuation-in-python/
    https://stackoverflow.com/questions/16060899/alphabet-range-in-python

    Decrypted Messages:
    Message 0 | Shift 4: the man who passes the sentence should swing the sword
    Message 1 | Shift 7: everyone is mine to torment
    Message 2 | Shift 1: you know nothing, jon snow
    Message 3 | Shift 4: that's what i do: i drink and i know things

    Encrypted Message:
    fqfx, n'r rtxy kfrnqnfw bnym otsfymfs afs sjxx' lfd tk ymwtsjx

'''

import string
EXCLUDE = list(string.digits + string.punctuation + string.whitespace)

def encrypt(message, shift):
    ''' Name: encrypt
        Inputs: message (str), shift amount (int)
        Returns: encrypted message (str)
    '''
    # call shift function to ensure valid shift is entered
    shift = check_max_shift(shift)

    # convert message is lowercase and create list from string
    message = message.lower()
    unencrypted_list = list(message)

    # convert character list to ascii values, applying encryption shift
    encrypted_list = encrypt_characters(unencrypted_list, EXCLUDE, shift)
    
    # convert ascii list to string of characters
    encrypted_string = convert_to_character(encrypted_list)

    return encrypted_string

def decrypt(message, shift):
    ''' Name: decypt
        Inputs: message (str), shift amount (int)
        Returns: decrypted message (str)
    '''
    # call shift function to ensure valid shift is entered
    shift = check_max_shift(shift)

    # convert message to lowercase and create list from string
    message = message.lower()
    encrypted_list = list(message)

    # convert character list to ascii values, applying decryption shift
    decrypted_list = decrypt_characters(encrypted_list, EXCLUDE, shift)

    # convert ascii list to string of characters
    decrypted_string = convert_to_character(decrypted_list)

    return decrypted_string
                
def check_max_shift(shift):
    ''' Name: check_max_shift
        Input: shift (int)
        Renturns: shift value as int unless over 25 then shift value of 1
    '''
    if shift > 25:
        shift = 1
    return shift

def encrypt_characters(char_list, excluded_characters, shift):
    ''' Name: encrypt_characters
        Input: list of characters and exclude characters, strings
        Returns: list of characters converted to ascii values with shift applied
    '''
    encrypted_list = []
    
    # iterate through each letter
    for i in range(len(char_list)):

        # convert chars to ascii, applying shift except spaces and punctuation
        if char_list[i] in excluded_characters:
            encrypted_list.append(ord(char_list[i]))
        else:
            unencrypted_val = ord(char_list[i])
            encrypted_val = unencrypted_val + shift

            # if shift = value over z, circle back to start of alphabet
            if encrypted_val > ord('z'):
                remainder = encrypted_val % ord('z')
                encrypted_val = remainder + ord('a') - 1
            encrypted_list.append(encrypted_val)

    return encrypted_list

def decrypt_characters(char_list, exclude_characters, shift):
    ''' Name: decrypt_characters
        Input: list of characters and exclude characters, strings
        Returns: list of characters convert to ascii values with shift applied
    '''
    decrypted_list = []

    # iterate through each letter
    for i in range(len(char_list)):

        # convert chars to ascii, applying shift except spaces and punctuation
        if char_list[i] in EXCLUDE:
            decrypted_list.append(ord(char_list[i]))
        else:
            encrypted_val = ord(char_list[i])
            decrypted_val = encrypted_val - shift

            # if shift = value less than a, circle back to end of alphabet
            if decrypted_val < ord('a'):
                remainder = ord("a") % decrypted_val
                decrypted_val = ord("z") - remainder + 1
            decrypted_list.append(decrypted_val)

    return decrypted_list

def convert_to_character(ascii_list):
    ''' Name: convert_to_character
        Input: list of ascii values (ints)
        Returns: string of ascii values converted to characters (strs)
    '''
    character_string = ""
    for i in range(len(ascii_list)):
        character_string += chr(ascii_list[i])
    return character_string
