import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())

graph = []
for i in range(n):
    graph.append(list(map(int, input().strip().split())))

# 섬에 숫자 달기
# 숫자 달고 0을 +1로 바꿔보기 