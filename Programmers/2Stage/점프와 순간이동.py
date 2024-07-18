### 첫풀이
# def solution(n):
#     ans = 0
#     dp = [0] * (n + 1)
#     dp[1] = 1
#     for i in range(2, n + 1):
#         # 점프
#         dp[i] = dp[i-1] + 1
#         # 순간이동
#         if i % 2 == 0:
#             dp[i] = min(dp[i//2], dp[i])
    
#     return dp[n]
def solution(n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            ans += 1
            n -= 1
    return ans
