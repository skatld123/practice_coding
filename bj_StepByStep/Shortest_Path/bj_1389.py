import sys

input = sys.stdin.readline
n, m = map(int, input().strip().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().strip().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n + 1):
    graph[i][i] = 1
    
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answers = []
for i in range(1, n + 1):
    answers.append(sum(graph[i]))

print(answers.index(min(answers)) + 1)