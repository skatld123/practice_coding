n = int(input().strip())

nlist = []
for i in range(n):
    nlist.append(list(map(int, input().strip().split())))

idxlist = [] 

for i in range(n):
    count = 1
    for j in range(n):
        if nlist[i][0] < nlist[j][0] and nlist[i][1] < nlist[j][1]:
            count += 1
    print(count, end=" ")
