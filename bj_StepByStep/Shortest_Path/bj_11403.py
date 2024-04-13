# 모든 정점이라고 했으니, 플로이드워셜로 작성
import sys

input = sys.stdin.readline
n = int(input().strip())
graph = []
for i in range(n):
    graph.append(list(map(int, input().strip().split())))
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] != 0 and graph[k][j] != 0:
                graph[i][j] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()