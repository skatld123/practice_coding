# 부품찾기
import sys

n = int(sys.stdin.readline().strip())
nlist = list(map(int, sys.stdin.readline().strip().split()))

nlist.sort()

m = int(sys.stdin.readline().strip())
mlist = list(map(int, sys.stdin.readline().strip().split()))
    
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (end + start) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

for m in mlist:
    print("yes" if binary_search(nlist, m, 0, n - 1) else "no", end=' ')
    
    
