import sys
input = sys.stdin.readline
nlist = list(input().strip())
slist = []
ilist = []
for i in range(len(nlist)):
    if nlist[i].isdigit():
        ilist.append(nlist[i])
    else:
        slist.append(nlist[i])
ilist.sort()
slist.sort()
print(''.join(slist + ilist))