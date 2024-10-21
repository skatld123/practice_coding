def solution(n, times):
    answer = 0
    start = 1
    end = max(times) * n
    while start <= end:
        mid = (start + end) // 2
        pt = 0
        for time in times:
            pt += mid // time
            if n <= pt:
                break
        if n <= pt:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
    return answer
