'''
    Nathanial Ziegler
    CS 5001
    February 12, 2020
    HW 5
    Description:
        Test function for calculate_word_frequency in test_functions file
'''

from classify_functions import calculate_word_frequency

TEST_1 = ["dog", "dog", "cat", "cat", "bird", "bird"]
EXPECTED_1 = [["dog", 2],["cat", 2],["bird", 2]]

TEST_2 = ["dog", "Dog", "dOg", "dog", "dOg"]
EXPECTED_2 = [["dog", 2],["Dog", 1],["dOg", 2]]

TEST_3 = ["Jim", "Alison", "Nick", "Nate", "Buddy"]
EXPECTED_3 = [["Jim", 1], ["Alison", 1], ["Nick", 1],
              ["Nate", 1], ["Buddy", 1]]

TEST_4 = ["a1", "a2", "a2", "a3", "a3", "a3", "a4", "a4", "a4", "a4",
          "a5", "a5", "a5", "a5", "a5", "a6", "a6", "a6", "a6", "a6","a6"]
EXPECTED_4 = [["a1", 1], ["a2", 2],["a3", 3], ["a4", 4], ["a5", 5], ["a6", 6]]

TEST_5 = ["123", "123", "123", "456", "456", "456", "789", "789", "789"]
EXPECTED_5 = [["123", 3], ["456", 3], ["789", 3]]
              
def test_word_frequency(word_list, expected):
    ''' Name: test_word_frequency
        Input: word_list (for one test) expected result of nested strings
               formatted : [["string", int],["string", int]
        Returns: nested list formated: [["word", count],["word", count]]
                 "word" = string and count = int
    '''
    print("Test Word List: ", word_list,"\n","Expected Results: ",
          expected, sep = "")
    actual = calculate_word_frequency(word_list)
    print("Actual Result:", actual)
    if actual == expected:
        print("Test passed!\n")
        return True
    print("Test Failed\n")
    return False
    
def test_all_word_frequency():
    ''' Name: test_all_word_frequency
        Input: none
        Returns: count of tests failed (int)
    '''
    count = 0

    # Test 1: TEST_1 and EXPECTED_1
    if not test_word_frequency(TEST_1, EXPECTED_1):
        count += 1
    # Test 2: TEST_2 and EXPECTED_2
    if not test_word_frequency(TEST_2, EXPECTED_2):
        count += 1
    # Test 1: TEST_3 and EXPECTED_3
    if not test_word_frequency(TEST_3, EXPECTED_3):
        count += 1
    # Test 1: TEST_4 and EXPECTED_4
    if not test_word_frequency(TEST_4, EXPECTED_4):
        count += 1
    # Test 1: TEST_5 and EXPECTED_5
    if not test_word_frequency(TEST_5, EXPECTED_5):
        count += 1

    return count

def main():

    count = test_all_word_frequency()
    if count > 0:
        print(count, "test failed. Please correct.")
    else:
        print("All tests passed!")

main()
