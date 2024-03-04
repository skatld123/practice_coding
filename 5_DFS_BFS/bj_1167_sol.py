# 임의의 점에서 가장 먼 점을 찾고, 그 점에서 가장 먼점이 트리의 지름이다
import sys
sys.setrecursionlimit(10**6)

def dfs(start_node, weight):
    for n, w in tree[start_node]:
        if dist[n] == -1:
            dist[n] = weight + w
            dfs(n, weight + w)
            
n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n):
    infos = list(map(int, input().split()))
    #  node_num, dest, distance 3 1 2 4 3 -1
    for i in range(len(infos)):
        if infos[i] == -1 : break
        if i % 2 == 1:
            tree[infos[0]].append((infos[i], infos[i + 1]))

dist = [-1] * (n + 1)
dist[1] = 0
dfs(1, 0)
# 1이라는 점에서 가장 거리가 먼 맨 끝점임
start = dist.index(max(dist))
dist = [-1] * (n + 1)
dist[start] = 0
dfs(start, 0)
print(max(dist))