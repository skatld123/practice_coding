def max_earnings(part_times):
    # 종료일을 기준으로 정렬
    part_times.sort(key=lambda x: x[1])

    # DP 배열 초기화
    dp = [0] * len(part_times)
    dp[0] = part_times[0][2]

    for i in range(1, len(part_times)):
        # 현재 파트타임의 수익
        current_profit = part_times[i][2]

        # 이전 파트타임 중 겹치지 않는 파트타임의 최대 수익 찾기
        for j in range(i - 1, -1, -1):
            if part_times[j][1] <= part_times[i][0]:  # 겹치지 않는 경우 찾기
                current_profit += dp[j]
                break

        # 이전까지의 최대 수익과 현재 선택한 경우의 최대 수익 중 더 큰 값을 저장
        dp[i] = max(dp[i - 1], current_profit)

    # 최대 수익 반환
    return max(dp)


# 테스트 케이스
part_times = [[3, 6, 3], [2, 4, 2], [10, 12, 8], [11, 15, 5], [1, 8, 10], [12, 13, 1]]
print(max_earnings(part_times))  # 결과: 19
