import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
# n=회사 개수, m=간선 개수
n, m = map(int, input().strip().split())
graph = [[INF] * (n + 1) for _ in range(n+1)]

for i in range(1, n + 1):
    graph[i][i] = 0
    
for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a][b] = 1
    graph[b][a] = 1
# x=최종목적지, k=경유해야하는 곳(소개팅)
x, k = map(int, input().strip().split())

# 여기 k는 입력받은 경유하는 k가 아님
# 각 노드를 경유했을 때를 가정하기 위한 k
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)