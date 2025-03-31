maxi, mini = 0, int(1e9)

prices = [3, 2, 4, 8, 7]

for i in prices:
    mini = min(mini, i)
    maxi = max(maxi, i - mini)

print(maxi if maxi > 0 else 0)