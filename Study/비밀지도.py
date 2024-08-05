def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        narr = arr1[i] | arr2[i]
        nbarr = list(format(narr, "b"))
        if len(nbarr) < n:
            nbarr = ["0"] * (n - len(nbarr)) + nbarr
        nlist = ""
        for j in range(len(nbarr)):
            if nbarr[j] == "1":
                nlist += "#"
            elif nbarr[j] == "0":
                nlist += " "
        answer.append(nlist)
    return answer
