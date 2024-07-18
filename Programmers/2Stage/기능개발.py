def solution(progresses, speeds):
    answer = []
    # i의 예상 작업 시간 < i-1, i-2, i-3..의 예상 작업 시간이라면 i는 i-1,i-2..중 의 예상 날짜에 배포
    # 예상 날짜 구하기, 100 - 9
    expected = []
    previous = 0
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        day = remain // speeds[i]
        if remain % speeds[i] > 0:
            day += 1
        expected.append(day)
    print(expected)
    s = 0
    for i in range(len(expected)):
        if expected[i] > expected[s]:
            answer.append(i-s)
            s = i
    answer.append(len(expected) - s)
            
    return answer