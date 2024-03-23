n, target = map(int, input().split())

cards = list(map(int, input().split()))

total = 0

for i in range(len(cards)):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cards[i] + cards[j] + cards[k] > target:
                continue
            else:
                total = max(total, cards[i] + cards[j] + cards[k])
print(total)