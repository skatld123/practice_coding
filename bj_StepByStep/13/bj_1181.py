# set은 중복요소 제거, sort는 기본적으로 문자열 정렬을 함
import sys
n = int(sys.stdin.readline())

words = []
for i in range(n):
    words.append(sys.stdin.readline().strip())

words = list(set(words))
words.sort()
words.sort(key=lambda x:(len(x)))

for w in words:
    print(w)