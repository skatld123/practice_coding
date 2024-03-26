import sys

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(1, n):
    for j in range(len(arr[i])):
        if 0 < j < len(arr[i]) - 1:
            arr[i][j] = max(arr[i - 1][j] + arr[i][j], arr[i - 1][j - 1] + arr[i][j])
        elif j == 0:
            arr[i][j] = arr[i - 1][j] + arr[i][j]
        else:
            arr[i][j] = arr[i - 1][j - 1] + arr[i][j]
print(max(arr[n - 1]))