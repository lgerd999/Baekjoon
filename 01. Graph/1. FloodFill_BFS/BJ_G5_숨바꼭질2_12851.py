# https://www.acmicpc.net/problem/12851
#

'''
숨바꼭질1에서 가장 빠른 시간을 찾을 수 있었고,
숨바꼭질4에서 그에 대한 경로를 찾을 수 있었음

'''

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def bfs():
    global ans
    Q = deque()
    Q.append(N)
    while Q:
        r = Q.popleft()
        
        if r == K:            
            ans += 1
            continue
                
        for nr in (r-1, r+1, r*2):
            if 0 <= nr <= 100000 :
                # 최소 시간이 같은 경우에도 Q에 추가될 수 있도록 함
                if not visited[nr] or visited[nr] == visited[r] +1:                
                    visited[nr] = visited[r] +1
                    Q.append(nr)                
       
N,K = map(int,input().split())        
visited = defaultdict(int)
ans = 0
bfs()
print(visited[K])
print(ans)