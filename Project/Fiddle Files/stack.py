'''
    CS5001
    Spring 2020
    Source code from lecture - the Stack class

    Four methods are implemented, in addition to the constructor:
    - push (adds a new element to the top of the stack)
    - pop (removes the top element from the stack)
    - top (returns, doesn't remove, the top element)
    - is_empty (return T/F indicating if the stack is empty)
'''

class Stack:
    def __init__(self):
        self.mystack = []

    def push(self, element):
        self.mystack.append(element)

    def pop(self):
        if self.mystack:
            self.mystack.pop()

    def top(self):
        if self.mystack:
            return self.mystack[-1]

    def is_empty(self):
        return not self.mystack
