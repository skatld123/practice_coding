# 시간초과가 발생한 풀이
# import sys
# n = sys.stdin.readline()

# nlist = list(map(int, sys.stdin.readline().strip().split()))
# slist = sorted(list(set(nlist)))

# for i in nlist:
#     if i in slist:
#         print(slist.index(i), end=' ')
        
# 아래와 같이 정정
import sys
n = sys.stdin.readline()

nlist = list(map(int, sys.stdin.readline().strip().split()))
slist = sorted(list(set(nlist)))

dic = {slist[i] : i for i in range(len(slist))}
for i in nlist:
    print(dic[i], end=' ')