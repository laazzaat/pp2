def uniqueList(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i) 
    return res

listik = list(map(int, input().split()))
print(uniqueList(listik))