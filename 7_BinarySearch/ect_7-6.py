import sys

n, m = map(int, sys.stdin.readline().strip().split())

cakes = list(map(int, sys.stdin.readline().strip().split()))

def binary_search(arrs, target, start, end):
    while start <= end:
        mid = (start + end) // 2 
        slices = 0
        for cake in arrs:
            if cake > mid:
                slices += (cake - mid)
        if slices == target:
            return mid
        elif slices > target:
            start = mid + 1
        else:
            end = mid - 1
    return None

print(binary_search(cakes, m, 0, max(cakes) - 1))