from stack import Stack

def convert_to_decimal(string):
    ''' Name: convert_to_decimal
        Input: a string of only digits
        Returns: an int (base-10 of value of what we converted)
    '''
    stack = Stack()
    decimal_result = 0
    place_value = 0
    
    for digit in string:
        stack.push(int(digit))

    while not stack.is_empty():
        decimal_result += (stack.top() * (2**place_value))
        stack.pop()
        place_value += 1

    return decimal_result
