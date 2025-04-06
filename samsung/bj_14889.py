n = int(input())
teamwork = []
for _ in range(n):
    teamwork.append(list(map(int, input().rstrip().split())))

isSplit = [False for _ in range(n)]
minimum = int(1e9)

def dfs(idx, count):
    global minimum
    if count == n // 2:
        point_start = 0
        point_link = 0
        for i in range(n):
            for j in range(n):
                if isSplit[i] and isSplit[j]:
                    point_start += teamwork[i][j]
                elif not isSplit[i] and not isSplit[j]:
                    point_link += teamwork[i][j]
        minimum = min(minimum, abs(point_start - point_link))
        return minimum
    else:
        for i in range(idx, n):
            if not isSplit[i]:
                isSplit[i] = True
                dfs(i + 1, count + 1)
                isSplit[i] = False

dfs(0, 0)
print(minimum)