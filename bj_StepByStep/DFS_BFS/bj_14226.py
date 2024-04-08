from collections import deque
s = int(input())

clipboard = 0
visited = [[False] * 2001 for _ in range(2001)]
# 1개가 기본적으로 있음
def bfs():
    # 이모지 개수와 시간, 클립보드 (1개, 0초)
    queue = deque([[1, 0, 0]])
    while queue:
        emojis, cnt, cp = queue.popleft()
        if emojis == s:
            return cnt
        # 클립보드 복사
        if not visited[emojis][emojis]:
            queue.append([emojis, cnt + 1, emojis])
            visited[emojis][emojis] = True
        #붙여넣기 emojis + cp <= s 부분이 이해가 잘 안감
        if emojis + cp <= s and not visited[emojis + cp][cp] and cp != 0:
            queue.append([emojis + cp, cnt + 1, cp])
            visited[emojis + cp][cp] = True
        # 삭제
        if emojis > 0:
            if not visited[emojis - 1][cp]:
                queue.append([emojis - 1, cnt + 1, cp])
                visited[emojis - 1][cp] = True
    return -1

print(bfs())
