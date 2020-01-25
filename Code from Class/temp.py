'''
    CS5001
    Spring 2020
    Sample code from class 1/8/20

    Test case:
        * celsius = 0, fahrenheit should be 32
        * celsius = 100, fahrenheit should be 212
    
'''

def main():
    celsius = float(input("What's the temp in celsius?\n"))
    fahrenheit = celsius * (9 / 5) + 32
    print("Temp in fahrenheit is", fahrenheit)
    
main()
