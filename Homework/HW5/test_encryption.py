'''
    CS5001
    Spring 2020
    HW5 test suite
    Test encrypt/decrypt functions
'''

from encryption import encrypt
from encryption import decrypt

def test_encrypt(msg, shift, expected):
    ''' Function test_encrypt
        Params: original msg (string), shift (int), expected encrypted version
        Returns: boolean, true if passed, false otherwise
        Does: calls the encrypt function and compares expected result
              to actual.
    '''
    print('Shifting', msg, 'by', shift, 'expecting', expected, '...')
    if encrypt(msg, shift) == expected:
        print('SUCCESS!')
        return True
    print('FAIL :(\n')
    return False

def test_decrypt(msg, shift, expected):
    ''' Function test_decrypt
        Params: encrypted msg (string), shift (int), expected decrypted version
        Returns: boolean, true if passed, false otherwise
        Does: calls the decrypt function and compares expected result
              to actual.
    '''
    print('Shifting back', msg, 'by', shift, 'expecting', expected, '...')
    if decrypt(msg, shift) == expected:
        print('SUCCESS!')
        return True
    print('FAIL :(\n')
    return False

def test_encrypt_decrypt(msg, shift):
    ''' Function test encrypt_decrypt
        Params: message (a string), a shift amount (int)
        Returns: boolean, true if passed, false otherwise
        Does: calls encrypt on the string, then decrypts and
              makes sure we got back the original.
    '''
    print('Encrypting/Decrypting', msg, 'by', shift)
    if decrypt(encrypt(msg, shift), shift) == msg:
        print('SUCCESS!')
        return True
    print('FAIL :(\n')
    return False

def run_encrypt_tests():
    ''' Function run_encrypt_tests
        Params: none
        Returns: an int, number of tests that failed
        Does: repeatedly calls test_encrypt, on a variety of
              strings/shifts, and counts num tests that passed/failed
    '''
    num_pass = 0
    num_fail = 0

    # Test One: Shift a by one, get b
    if test_encrypt('a', 1, 'b'):
        num_pass += 1
    else:
        num_fail += 1

    # Test Two: Shift ab by 5, get fg
    if test_encrypt('ab', 5, 'fg'):
        num_pass += 1
    else:
        num_fail += 1

    # Test Three: Shift z by 1, wraparound and get a
    if test_encrypt('a', 1, 'b'):
        num_pass += 1
    else:
        num_fail += 1

    # Test Four: Shift by 26 (too big), should fall back to 1
    if test_encrypt('x', 26, 'y'):
        num_pass += 1
    else:
        num_fail += 1

    # Test Five: Shift pizza by 3, get slccd
    if test_encrypt('pizza', 3, 'slccd'):
        num_pass += 1
    else:
        num_fail += 1

    # Test Six: Shift Z by 25, get y
    if test_encrypt('Z', 25, 'y'):
        num_pass += 1
    else:
        num_fail += 1

    # Test Seven: Shift ABC by 12, get mno
    if test_encrypt('ABC', 12, 'mno'):
        num_pass += 1
    else:
        num_fail += 1

    # Test Eight: Shift ABC by 0, get abc
    if test_encrypt('ABC', 0, 'abc'):
        num_pass += 1
    else:
        num_fail += 1

    # Test Nine: Shift a!!## by 1, ignore the punctuation
    if test_encrypt('a!!##', 1, 'b!!##'):
        num_pass += 1
    else:
        num_fail += 1

    return num_fail

def run_decrypt_tests():
    ''' Function run_decrypt_tests
        Params: none
        Returns: an int, number of tests that failed
        Does: repeatedly calls test_encrypt, on a variety of
              strings/shifts, and counts num tests that passed/failed
    '''
    num_pass = 0
    num_fail = 0

    # Test One: Shift b by one, get a
    if test_decrypt('b', 1, 'a'):
        num_pass += 1
    else:
        num_fail += 1

    # Test Two: Shift fg by 5, get ab
    if test_decrypt('fg', 5, 'ab'):
        num_pass += 1
    else:
        num_fail += 1

    # Test Three: Shift a by 1, wraparound and get z
    if test_decrypt('a', 1, 'z'):
        num_pass += 1
    else:
        num_fail += 1

    # Test Four: Shift  y by 26 (too big), should fall back to 1
    if test_decrypt('y', 26, 'x'):
        num_pass += 1
    else:
        num_fail += 1

    # Test Five: Shift slccd by 3, get pizza
    if test_decrypt('slccd', 3, 'pizza'):
        num_pass += 1
    else:
        num_fail += 1

    # Test Six: Shift Y by 25, get z
    if test_decrypt('Y', 25, 'z'):
        num_pass += 1
    else:
        num_fail += 1

    # Test Seven: Shift MNO by 12, get abc
    if test_decrypt('MNO', 12, 'abc'):
        num_pass += 1
    else:
        num_fail += 1

    # Test Eight: Shift ABC by 0, get abc
    if test_decrypt('ABC', 0, 'abc'):
        num_pass += 1
    else:
        num_fail += 1

    # Test Nine: Shift a$$!! by 0, geta$$!! (ignore punct)
    if test_decrypt('a$$!!', 0, 'a$$!!'):
        num_pass += 1
    else:
        num_fail += 1

    return num_fail

def run_encrypt_decrypt_tests():
    ''' Function run_encrypt_decrypt_tests
        Params: none
        Returns: an int, number of tests that failed
        Does: repeatedly encrypts, then decrypts a msg,
              making sure we got back the original
    '''
    num_pass = 0
    num_fail = 0

    # Test One: Shift a by 1
    if test_encrypt_decrypt('a', 1):
        num_pass += 1
    else:
        num_fail += 1

    # Test Two: Shift ab by 5
    if test_encrypt_decrypt('ab', 5):
        num_pass += 1
    else:
        num_fail += 1

    # Test Three: Shift pizza by 3
    if test_encrypt_decrypt('pizza', 3):
        num_pass += 1
    else:
        num_fail += 1

    # Test Four: Shift !hello? by 24
    if test_encrypt_decrypt('!hello?', 24):
        num_pass += 1
    else:
        num_fail += 1

    return num_fail


def main():
    # Run all the tests to encrypt first, and report results
    print('Testing the encrypt function...')
    num_failed = run_encrypt_tests()
    if num_failed == 0:
        print('ALL TESTS PASSED, NICE WORK!!!\n')
    else:
        print(num_failed, 'tests failed, pls go back and fix\n')

    # Run all the tests to decrypt, and report results
    print('Testing the decrypt function...')
    num_failed = run_decrypt_tests()
    if num_failed == 0:
        print('ALL TESTS PASSED, NICE WORK!!!\n')
    else:
        print(num_failed, 'tests failed, pls go back and fix.\n')

    # Finally, run the tests that encrypt, decrypt, and make sure
    # we get back the original
    print('Testing the encrypt/decrypt sequence...')
    num_failed = run_encrypt_decrypt_tests()
    if num_failed == 0:
        print('ALL TESTS PASSED, NICE WORK!!!\n')
    else:
        print(num_failed, 'tests failed, pls go back and fix.\n')

    print('Testing complete!')
    

main()
    
    
