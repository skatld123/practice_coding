import sys
n = int(sys.stdin.readline())

points = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    points.append((x, y))

points.sort(key=lambda x:(x[1], x[0]))

for x1, y1 in points:
    print(f'{x1} {y1}')