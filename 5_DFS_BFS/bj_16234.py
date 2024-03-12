# from collections import deque
# n, l, r = map(int, input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))

# dx = [0, 0, -1 , 1]
# dy = [-1, 1, 0, 0]
# result = 0

# def bfs(x, y, index):
#     queue = deque()
#     v = queue.popleft()
#     united = []
#     while True: