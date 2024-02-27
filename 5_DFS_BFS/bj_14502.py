# 세로 n, 가로 m
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    
# def dfs(x, y) :
    