n = int(input())

dp = [[0] * 10 for _ in range(n)]
# 각 자리수의 해당되는 것부터 차례대로 경우의 수를 생각해볼 것
for i in range(n):
    for j in range(10):
        # 첫번째 자리수가 0일 때를 제외하고 모두 1로 초기화
        if i == 0:
            if j != 0: dp[i][j] = 1
        else:
            # 9일때는 8밖에 없음 이동할 수 있는 것이
            if j == 9:
                dp[i][j] = dp[i-1][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j+1]
            else:
                # 두번째 자리에서 부터는 -1과 +1의 숫자일 때의 경우의 수를 합치기
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[n-1]) % 1000000000)