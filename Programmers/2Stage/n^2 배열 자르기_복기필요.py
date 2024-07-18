# 시간초과된 문제, 규칙을 찾을 것
def solution(n, left, right):
    # [1, 2, 3] [0, 1, 2] [(0,0), (0,1), (0,2)]
    # [2, 2, 3] [3, 4, 5] [(1,0), (1,1), (1,2)]
    # [3, 3, 3] [6, 7, 8] [(2,0), (2,1), (2,2)]
    line = []
    for num in range(left, right + 1):
        line.append(max(num // n, num % n) + 1)
    return line