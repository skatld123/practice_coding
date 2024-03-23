import sys
n = int(sys.stdin.readline())

members = []
for i in range(n):
    age, name = sys.stdin.readline().strip().split()
    members.append((i, int(age), name))

members.sort(key=lambda x:(x[1], x[0]))
for i, age, name in members:
    print(f'{age} {name}')