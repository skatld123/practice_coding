import sys
nlist = list(sys.stdin.readline().strip())
nlist = list(map(int, nlist))
nlist.sort(reverse=True)
result = ''.join(map(str, nlist))
print(result)