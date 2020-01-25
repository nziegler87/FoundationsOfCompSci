'''
    Nathanial Ziegler
    CS5001
    Homework 2
    January 21, 2020
    Description:
        Tests convert_lat, convert_long, and calc_distance functions found in
        boston.py.
'''
from boston import *

import math

def test_lat(LAT0, test_lat, expected):
    ''' Function: test_lat
        Input: Values to pass to convert_lat for one test: test_lat (float),
               LAT0 (float), and float for expected output
        Returns: Nothing
        Does: Calls convert_lat with given input. Prints expected and actual
              results so they can be compared.
    '''
    # Print inputs and expected value
    print("Input tested:\t", test_lat, "(lat)\t", LAT0, "(LAT0)",
          "\nExpected value:\t", expected, sep = "")

    # Calculate actual value returned from function
    actual = convert_lat(LAT0, test_lat)

    # Print actual value
    print("Actual value:\t", round(actual, 3), "\n", sep = "")

def test_long(LAT0, LONG0, test_lat, test_long, expected):
    ''' Function: test_long
        Input: Values to pass to convert_long for one test:
               LAT0, LONG0, test_lat, and test_long(floats)
               and expected output (float)
        Returns: Nothing
        Does: Calls convert_long with given inputs. Prints expected and
              actual results so they can be compared
    '''
    # Print inputs and expected value
    print("Input tested:\t", test_lat, "(lat)\t",test_long, "(long)\n",
          "\t\t", LAT0, "(LAT0)\t", LONG0, "(LONG0)\n"
          "Expected value:\t", expected, sep = "")

    # Calculate actual value returned from function
    actual = convert_long(LAT0, LONG0, test_lat, test_long)

    # Print actual value
    print("Actual value:\t", round(actual, 3), "\n", sep = "")

def test_distance(LAT0, LONG0, test_lat, test_long, expected):
    ''' Function: test_distance
        Input: Values to pass to calc_distance for one test:
               LAT0, LONG0, test_lat, and test_long as floats plus
               expected value as float
        Returns: Nothing
        Does: Calls calc_distance with given inputs. Prints expected and
              actual results so they can be compared
    '''
    # Print inputs and expected value
    print("Inputs tested:\t", test_lat, "(lat)\t", test_long,
          "(long)\n\t\t", LAT0, "(LAT0)\t", LONG0, "(LONG0)\n",
          "Expected value:\t", expected, sep = "")

    # Calculate actual value returned from function
    actual = calc_distance(LAT0, LONG0, test_lat, test_long)

    # Print actual value
    print("Actual value:\t", round(actual, 3), "\n", sep = "")

def main():

    # Testing of convert_lat
    print("--Tests of convert_lat--")

    # Test 1 - Input: LAT0, 42.3466803; Expected output: 90.070
    test_lat(LAT0, 42.3466803, 90.07)

    # Test 2 - Input: 42.356217; Expected output: 196.033
    test_lat(LAT0, 42.356217, 196.033)
    
    # Test 3 - Input: 42.316928; Expected output: -240.511
    test_lat(LAT0, 42.316928, -240.511)
    
    # Test 4 - Input: 42.323129; Expected output: -171.611
    test_lat(LAT0, 42.323129, -171.611)


    # Testing of convert_long
    print("\n--Tests of convert_long--")

    # Test 1 - Input: LAT0, LONG0, 42.3466803, -71.0994118
    #          Expected output: -39.950
    test_long(LAT0, LONG0, 42.3466803, -71.0994118, -39.950)

    # Test 2 - Input: LAT0, LONG0, 42.356217, -71.065510
    #          Expected output: -238.547
    test_long(LAT0, LONG0, 42.356217, -71.065510, 238.547)

    # Test 3 - Input: LAT0, LONG0, 42.316928, -71.120607
    #          Expected output :-214.127
    test_long(LAT0, LONG0, 42.316928, -71.120607, -214.127)

    # Test 4 - Input: LAT0, LONG0, 42.323129, -71.062206
    #          Expected output: 265.758
    test_long(LAT0, LONG0, 42.323129, -71.062206, 265.758)


    # Testing of calc_distance
    print("\n--Tests of calc_distance--")
    
    # Test 1 - Inputs: LAT0, LONG0, 42.3466803, -71.0994118
    #          Expected output: 0.895
    test_distance(LAT0, LONG0, 42.3466803, -71.0994118, 0.895)

    # Test 2 - Inputs: LAT0, LONG0, 42.356217, -71.065510
    #          Expected output: 1.959
    test_distance(LAT0, LONG0, 42.356217, -71.065510, 1.959)

    # Test 3 - Inputs: LAT0, LONG0, 42.316928, -71.120607
    #          Expected output: 2.396
    test_distance(LAT0, LONG0, 42.316928, -71.120607, 2.396)

    # Test 4 - Inputs: LAT0, LONG0, 42.323129, -71.062206
    #          Expected output: 1.723
    test_distance(LAT0, LONG0, 42.323129, -71.062206, 1.723) 
main()
