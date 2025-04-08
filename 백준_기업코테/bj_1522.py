ab_string = input().strip()

cnt_a = ab_string.count('a')

minimum = int(1e9)

for i in range(len(ab_string)):
    cnt_change = 0
    for j in range(cnt_a):
        idx = i + j
        if idx > len(ab_string) - 1:
            idx -= len(ab_string)
        if ab_string[idx] == 'b':
            cnt_change += 1
    minimum = min(minimum, cnt_change)

print(minimum)