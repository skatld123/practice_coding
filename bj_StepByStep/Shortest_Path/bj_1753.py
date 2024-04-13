import sys

input = sys.stdin.readline
n = int(input().strip())
m = int(input().strip())
graph = [[0] *(n + 1) for _ in range(n + 1)]

for i in range(m):
    heavy, light = map(int, input().strip().split())
    # heavy->light면 더 가벼운거면 -1
    graph[heavy][light] = 1
    
for i in range(1, n + 1):
    graph[i][i] = 1
    
# 중간에 껴있는 애들, 추론가능한 애들이 K네
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] =1

for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if not graph[i][j] and not graph[j][i]:
            cnt += 1
    print(cnt)