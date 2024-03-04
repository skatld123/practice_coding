from collections import deque

points = int(input())
graph = [[]]
distance = [[]]
for p in range(points):
    infos = list(map(int, input().split()))
    #  node_num, dest, distance
    graph.append([infos[i] for i in range(len(infos)) if i % 2 == 0 and i != 0 and i != len(infos) - 1])
    distance.append([infos[i] for i in range(len(infos)) if i % 2 == 1 and i != 0 and i != len(infos) - 1])

dist_from_start = [0 for i in range(len(graph))]

def bfs(start, graph, visited, dists):
    max_distance = 0
    visited[start] = True
    queue = deque[start]
    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                max_distance += dists[node]
                visited[node] = True