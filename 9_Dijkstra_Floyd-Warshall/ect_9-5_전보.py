import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().strip().split())
# 노드
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().strip().split())
    # 도착지와 시간
    graph[x].append((y, z))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최단 거리를 가진 노드
        dist, now = heapq.heappop(q)
        #기록된 거리보다 큰 경우 (최소거리가 아님)
        if distance[now] < dist: 
            continue
        # 현재 노드와 인접한 노드들
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐, 다른 노드까지의 이동하는 거리가 짧은 경우
            if cost < distance[i[0]]: 
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(c)
# 도달할 수 있는 노드의 수
count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        # 노드 중 가장 먼 노드를 하면, 그 시간내로 가까운 노드는 다 퍼지기에
        max_distance = max(max_distance, d)

print(count - 1, max_distance)