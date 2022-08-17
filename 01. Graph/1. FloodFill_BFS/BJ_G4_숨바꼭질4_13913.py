# https://www.acmicpc.net/problem/13913
# 
'''
숨바꼭질1과 차이점 : 경로 출력
숨바꼭질3과 차이점 : 주어진 조건 중 순간이동하는 경우 0초후 2*X 의 위치로 이동할 수 있음
숨바꼭질2와 차이점 : 가장 빠른 시간으로 찾는 방법의 수 계산 추가

'''

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def bfs():
    Q = deque()
    Q.append(N)
    while Q:
        r = Q.popleft()
        
        if r == K:
            print(visited[r])
            for _ in range(visited[r]+1):
                path.append(r)
                r = trace[r]            
            return 1
                
        for nr in (r-1, r+1, r*2):
            if 0 <= nr <= 100000 and not visited[nr] :                
                visited[nr] = visited[r] +1
                Q.append(nr)                
                trace[nr] = r
        
        # print(visited)  
    return 0

N,K = map(int,input().split())        
visited = defaultdict(int)
trace = defaultdict(int)
path = []
bfs()
# print(*path[::-1])
path.reverse()
print(*path)