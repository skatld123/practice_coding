import sys
from collections import deque
input = sys.stdin.readline

s = input().strip()
t = input().strip()

# 문자열 뒤에 A 추가
# 문자열 뒤에 B 추가 후 문자열 뒤집기
# 가능한지 확인, 가능하면 1 없으면 0

# 문자열 개수 이상이 되면 못만드는 것임
# def bfs():
#     queue = deque([])
#     queue.append(s)

#     while queue:
#         qstr = queue.popleft()

#         if len(qstr) == len(t):
#             if qstr == t:
#                 return True
#             else:
#                 continue
#         # 연산 1
#         queue.append(qstr + "A")
#         # 연산 2
#         bstr = qstr + "B"
#         queue.append(bstr[::-1])

# print(1 if bfs() else 0)

# 해당 코드 메모리 초과

# 반대로 진행
# 문자열을 뒤집고 뒤에 있는 B를 제거
# 문자열 뒤에 있는 a를 제거

def bfs():
    queue = deque([])
    queue.append(t)

    while queue:
        qstr = queue.popleft()

        if len(qstr) == len(s):
            if qstr == s:
                return True
            else:
                continue
        if qstr[-1] == 'A':
            # 연산 1 # 문자열 뒤에 있는 a를 제거
            queue.append(qstr[:-1])
        # 연산 2 # 문자열을 뒤집고 뒤에 있는 B를 제거
        if qstr[0] == 'B':
            bstr = qstr[::-1]
            queue.append(bstr[:-1])

print(1 if bfs() else 0)
