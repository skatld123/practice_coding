def solution(elements):
    answer = 0
    total_list = []
    elements = elements * 2
    # [7, 9, 1, 1, 4, 7, 9, 1, 1, 4]
    dp = [0] * (len(elements))
    dp[0] = elements[0]
    for i in range(1, len(elements)):
        dp[i] = dp[i - 1] + elements[i]
    # 수열 길이에 따라 뺄셈을 계산하고 total_list에 추가 
    for i in range(1, (len(elements) // 2 + 1)):
        for j in range(0, len(elements) // 2):
            num = dp[j + i] - dp[j]
            total_list.append(num)
    answer = len(list(set(total_list)))
    return answer