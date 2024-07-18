def solution(citations):
    answer = 0
    citations.sort()
    # for문을 돌면서, citations[i]번 이상인 개수가 몇개인지를 확인하고, 해당 개수와 i가 동일한지 확인
    # [1] -> 1회 이상, 1편 이상
    # cnt -> 인용횟수 i 이상인 개수
    for i in range(1, len(citations) + 1):
        cnt = 0
        for j in range(len(citations)):
            if i <= citations[j]:
                cnt += 1
        if cnt >= i:
            answer = i
    return answer