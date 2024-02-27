from collections import deque
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    snode, fnode = list(map(int, input().split()))
    graph[snode].append(fnode)
    graph[fnode].append(snode)
    graph[snode].sort()
    graph[fnode].sort()
    
def dfs(start_node, graph, visited):
    visited[start_node] = True
    print(start_node, end=' ')
    for node in graph[start_node]:
        if not visited[node]:
            dfs(node, graph, visited)

def bfs(start_node, graph, visited):
    queue = deque([start_node])
    visited[start_node] = True
    while queue: 
        vq = queue.popleft()
        print(vq, end=' ')
        for node in graph[vq]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
                
visited = [False] * (n + 1)
dfs(v, graph, visited)
print('')
visited = [False] * (n + 1)
bfs(v, graph, visited)