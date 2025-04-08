import sys
from collections import deque
input = sys.stdin.readline

string = list(input().strip())
string = deque(string)

explode = list(input().strip())

stack = []

for i in string:
    stack.append(i)
    if stack[len(stack)-len(explode):len(stack)] == explode:
        for _ in range(len(explode)):
            stack.pop()
if stack:
    print(*stack, sep='')
else:
    print("FRULA")
