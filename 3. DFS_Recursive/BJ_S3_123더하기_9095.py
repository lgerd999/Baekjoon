# https://www.acmicpc.net/problem/9095

def add123(csum,path):
    global cnt
    
    if csum < 0:
        return
    
    if csum == 0:
        result.append(path)

    for i in range(1,4):
        add123(csum-i,path+[i])

T = int(input())
for _ in range(T):
    result = []
    n = int(input())

    add123(n,[])
    print(len(result))