n = int(input())

num_list = list(map(int, input().split()))
sum, sub, mul, div = list(map(int, input().split()))
maximum = -int(1e9)
minimum = int(1e9)

def dfs(index, result, sum, sub, mul, div):
    global maximum, minimum
    if index == n :
        maximum = max(maximum, result)
        minimum = min(minimum, result)
        return
    next_num = num_list[index]
    if sum > 0:
        sum -= 1
        dfs(index + 1, result + next_num, sum, sub, mul, div)
        sum += 1
    if sub > 0:
        sub -= 1
        dfs(index + 1, result - next_num, sum, sub, mul, div)
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(index + 1, result * next_num, sum, sub, mul, div)
        mul += 1
    if div > 0:
        div -= 1
        dfs(index + 1, int(result / next_num), sum, sub, mul, div)
        div += 1
        
dfs(1, num_list[0], sum, sub, mul, div)
print(maximum)
print(minimum)