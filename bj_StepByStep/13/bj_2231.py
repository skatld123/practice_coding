import sys
n = int(sys.stdin.readline())
generators = []
for i in range(n, 0, -1):
    num_list = [i]
    while i != 0:
        num_list.append(i%10)
        i = i//10
    if sum(num_list) == n:
        generators.append(num_list[0])
        
if generators:
    print(min(generators))
else:
    print(0)