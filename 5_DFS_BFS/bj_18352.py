from collections import deque

def bfs(graph, start, visited, dist):
    ans = []
    queue = deque([start])
    visited[start] = True
    dist[start] = 0
    while queue :
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                dist[i] = dist[v] + 1
                if dist[i] == k :
                    ans.append(i)
    if len(ans) == 0:
        print('-1')
    else :
        for an in ans:
            print(an)
# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, input().split())

graph = []
for i in range(n + 1):
    graph.append([])
for i in range(m):
    bridge = list(map(int, input().split()))
    index = bridge[0]
    graph[index].append(bridge[1])

visited = [False] * (n + 1)
dist = [0] * (n + 1)
bfs(graph, 1, visited, dist)


