from stack import Stack
from bball import BBallPlayer
from part2 import equal_stacks

s1 = Stack()
s1.push(BBallPlayer('bird', 81))
s1.push(BBallPlayer('drj', 79))
s1.push(BBallPlayer("nate", 98))

s2 = Stack()
s2.push(BBallPlayer('bird', 81))
s2.push(BBallPlayer('drj', 79))
s2.push(BBallPlayer("jimmy", 98))

print(equal_stacks(s1, s2))

s3 = Stack()
s3.push(BBallPlayer('shaq', 85))
s3.push(BBallPlayer('jordan', 78))

s4 = Stack()
s4.push(BBallPlayer('shaq', 88))
s4.push(BBallPlayer('jordan', 78))

print(equal_stacks(s3, s4))
