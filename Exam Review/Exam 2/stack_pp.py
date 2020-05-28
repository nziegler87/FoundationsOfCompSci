from stack import Stack


def convert_to_binary(number):
    stack = Stack()
    div = number

    while div > 0:
        stack.push(div % 2)
        div = div // 2

    if number == 0:
        return 0

    result = ""
    while not stack.is_empty():
        result += str(stack.top())
        stack.pop()
    print(result)
        
def test_balance(string):
    stack = Stack()
    for char in string:
        if char == "(":
            stack.push("(")

    for char in string:
        if char == ")":
            if stack.is_empty():
                return False
            else:
                stack.pop()

    if stack.is_empty():
        return True
    else:
        return False
        

def reverse(string):
    stack = Stack()
    reverse = ""
    for char in string:
        stack.push(char)

    while not stack.is_empty():
        reverse += str(stack.top())
        stack.pop()

    print(reverse)

def reverse2(string):
    if not string:
        return ""
    else:
        return string[-1] + reverse2(string[:-1])

def reverse3(string):
    if not string:
        return ""
    else:
        return reverse2(string[1:]) + string[0]
