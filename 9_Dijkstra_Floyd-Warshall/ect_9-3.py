# 플로이드 워셜 알고리즘 
INF = int(1e9)

n = int(input())
m = int(input())
# 1. 2차원 리스트, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 입력: 각 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따른 플로이드 워셜 알고리즘
# k는 거쳐가는 노드, a 출발 노드, b 도착 노드
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
# 결과출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()