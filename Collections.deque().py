from collections import deque

d = deque()
n = int(input())

for _ in range(n):
    command = input().split()
    if len(command) == 1:
        getattr(d, command[0])()
    else:
        getattr(d, command[0])(command[1])

print(' '.join(d))
