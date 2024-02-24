def dfs(dw, dh): 
    global w, h
    if dw < 0 or dw >= w or dh < 0 or dh >= h :
        return False
    if maps[dh][dw] == 1 :
        maps[dh][dw] = 0
        dfs(dw - 1, dh)
        dfs(dw + 1, dh)
        dfs(dw, dh - 1)
        dfs(dw, dh + 1)
        dfs(dw - 1, dh - 1)
        dfs(dw - 1, dh + 1)
        dfs(dw + 1, dh - 1)
        dfs(dw + 1, dh + 1)
        return True
    return False

results = []
while True : 
    w, h = map(int, input().split())
    
    if w == 0 and h == 0 :
        for res in results :
            print(res)
        break
    
    maps = []
    for nh in range(h) :
        maps.append(list(map(int, input().split())))
    
    result = 0
    for ih in range(h) :
        for iw in range(w) :
            if dfs(iw, ih) == True :
                result += 1
    results.append(result)
