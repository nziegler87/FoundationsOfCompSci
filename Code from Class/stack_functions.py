from stack import Stack

def convert_to_binary(integer):
    stack = Stack()
    binary = ""

    if integer < 0:
        return ""

    if integer == 0:
        return str(0)

    else:
        while integer > 0:
            stack.push(str(integer % 2))
            integer = integer // 2

    while not stack.is_empty():
        binary += stack.top()
        stack.pop()

    return binary

def is_balanced(string):
    punct = Stack()
    for char in string:
        if char == "(":
            punct.push(char)
        if char == ")":
            if punct.is_empty():
                return False
            if punct.top() == "(":
                punct.pop()
    if not punct.is_empty():
        return False
    else:
        return True

    
    
