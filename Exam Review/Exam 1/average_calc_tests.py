from average_calc_functions import calculate_mean

TEST_1 = [2, 2, 2]
EXPECTED_1 = 2

TEST_2 = [2, 4, 6]
EXPECTED_2 = 4

def test_calculate_mean(input_list, expected):
    actual = calculate_mean(input_list)
    print("Input list:", input_list, "\nExpected Mean:", expected,
          "\nActual Result:", actual)
    if actual == expected:
        return True

def test_all():
    count = 0
    # test 1
    if not test_calculate_mean(TEST_1, EXPECTED_1):
        count += 1
    if not test_calculate_mean(TEST_2, EXPECTED_2):
        count += 1
    return count

def main():
    count = test_all()
    if count == 0:
        print("All tests passed!")
    else:
        print(count, "tests failed.")

main()
    
