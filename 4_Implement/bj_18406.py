import sys
input = sys.stdin.readline

nlist = list(map(int, input().strip()))

a = sum(nlist[:len(nlist)//2])
b = sum(nlist[len(nlist)//2:])
if a == b:
    print("LUCKY")
else:
    print("READY")