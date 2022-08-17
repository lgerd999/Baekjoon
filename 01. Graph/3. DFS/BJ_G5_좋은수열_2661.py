# https://www.acmicpc.net/problem/2661
# https://velog.io/@ckstn0778/%EB%B0%B1%EC%A4%80-2661%EB%B2%88-%EC%A2%8B%EC%9D%80%EC%88%98%EC%97%B4-O-1-Python

def check(result,addStr):
    temp = "".join(result) + addStr
    for i in range(1, len(temp) // 2 + 1):
        print(temp)
        # print(temp[-2 * i : -1 * i],temp[-1 * i :])

        if temp[-2 * i : -1 * i] == temp[-1 * i :]:
            return False
    return True

def dfs():
    global result
    if len(result) == N:
        print(str.join('',result))
        print(result)
        exit()

    for i in range(1, 4):
        if check(result, str(i)):
            result.append(str(i))
            dfs()            
            result.pop() # 추가했던 문자를 삭제

N = int(input())
result = []
dfs()