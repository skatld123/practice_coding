from collections import deque

def solution(n, computers):
    answer = 0
    graph = []
    visited = [False] * n
    for i in range(n):
        line = []
        for j in range(n):
            if i != j and computers[i][j] == 1:
                line.append(j)
        graph.append(line)
    for i in range(n):
        if not visited[i]:
            answer += bfs(i, visited, graph)
    
    return answer

def bfs(start, visited, graph):
    queue = deque([start])
    visited[start] = True
    while queue:
        q = queue.popleft()
        for next_node in graph[q]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
    return 1