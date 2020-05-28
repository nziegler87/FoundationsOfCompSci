from stack import Stack

def main():
    stack = Stack()
    stack.push(4)
    stack.push(8)
    stack.pop()
    print(stack.top())
    stack.push(4)
    print(stack.top())
    stack.pop()
    print(stack.top())

main()
