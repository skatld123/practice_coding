from collections import deque
def solution(k, dungeons):
    answer = -1
    # [최소 필요 피로도, >  소모 피로도]
    # 가장 많이 돌려면, 소모 피로도가 적은 순으로 가야하지만, 최소 필요 피로도가 큰 순으로도 가야함
    # -> 나오는 숫자에 따라 어떻게 될지 모름
    # 따라서, 모든 경우의 수를 해봐야 함
    for i in range(len(dungeons)):
        answer = max(answer, bfs(i, k, dungeons))
    return answer

def bfs(num, stats, dungeons):
    queue = deque([])
    queue.append([[num], stats - dungeons[num][1]]) # 던전 순차 경로를 [num]으로 입력
    cnt = -1
    while queue:
        qn, qstats = queue.popleft()
        for i in range(len(dungeons)):
            d_need, d_minus = dungeons[i]
            if not i in qn and qstats >= d_need:
                queue.append([qn + [i], qstats - d_minus])
                cnt = max(cnt, len(qn + [i]))
    return cnt