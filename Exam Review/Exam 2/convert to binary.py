from stack import Stack

def convert_binary(decimal):
    stack = Stack()

    remainder = 0

    if decimal == 0:
        return 0

    while decimal >= 1:
        stack.push(decimal % 2)
        decimal = decimal // 2

    new = ""
    
    while not stack.is_empty():
        new += str(stack.top())
        stack.pop()

    return new
