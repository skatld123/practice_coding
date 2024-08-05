from collections import deque


def solution(n, s, a, b, fares):
    answer = 0
    # n 지점개수, s 출발지점, a 도착지점, b 도착지점
    # fare [c, d, f] c와 d사이는 f요금
    # 각 node list를 구현하되, 내부에는 [(목적지1, 요금1), (목적지2, 요금2), ..]으로 구성되도록
    # 최적 경로를 작성해볼 것?
    # 일단 S에서 각 노드로 한칸 가고, 거기서 A, B까지의 최적 경로를 계산해보기?
    # DP를 이용하여 각 노드 별 S에서의 최적 경로를 계산
    grp = [[] for _ in range(n + 1)]

    for i in range(len(fares)):
        c, d, f = fares[i]
        grp[c].append((d, f))
        grp[d].append((c, f))
    dp = cal_minlength(grp, n, s)
    # print(dp)
    minimum = dp[a] + dp[b]
    for i in range(len(dp)):
        if i == s:
            continue
        else:
            idp = cal_minlength(grp, n, i)  # i에서 시작했을 때의 dp
            # print(f"minimum, dp[{i}] + idp[{a}] + idp[{b}] : \n {minimum}, {dp[i]} + {idp[a]} + {idp[b]}")
            minimum = min(minimum, (dp[i] + idp[a] + idp[b]))
            print(minimum)
    return minimum


def cal_minlength(grp, n, s):
    dp = [int(1e8)] * (n + 1)
    visited = [False] * (n + 1)
    dp[s] = 0
    queue = deque([])
    queue.append(s)
    while queue:
        qnode = queue.popleft()
        for i in range(len(grp[qnode])):
            nxt_node, fee = grp[qnode][i]
            if dp[nxt_node] > dp[qnode] + fee:
                dp[nxt_node] = dp[qnode] + fee  # S에서의 최솟값으로 다 변환
                queue.append(nxt_node)
    return dp
