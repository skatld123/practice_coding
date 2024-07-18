def solution(n, words):
    answer = []
    # 그 다음 for문으로 하나씩 글자를 비교, 또 안에 있는지 확인
    # 번호, 차례를 return
    isPerfect = True
    for i in range(1, len(words)):
        if words[i][0] != words[i - 1][-1] or words[i] in words[:i]:
            isPerfect = False
            answer = [(i % n) + 1,(i // n) + 1]
            break
        else:
            continue
    if isPerfect:
        answer = [0,0]
    return answer