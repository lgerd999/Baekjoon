# https://www.acmicpc.net/problem/13549
# 
'''
1초 후 X-1, X+1 이동
0초 후 X*2로 이동

appendleft : deque의 맨앞에 데이터를 추가
append : deque의 맨뒤에 데이터를 추가
'''

import sys
from collections import deque,defaultdict

input = sys.stdin.readline

def bfs():
    Q = deque()
    Q.append(N)  # 수빈이 위치
    while Q:
        r = Q.popleft()
        if r == K:  # 수빈이 위치와 동생 위치가 같게 되면.
            return visited[r]        
        
        # 리스트 (r-1, r+1, r*2) 3가지 이동 방법에 대해 반복
        for nr in (r-1,r+1,r*2):                 
            if 0 <= nr < 100001 and not visited[nr]:
                # nr == 2*r이 되는 시점은 이동 시간이 0초이므로 visited[r]과 동일하게 설정.
                if nr == 2*r and nr != 0:
                    visited[nr] = visited[r]                    
                    Q.appendleft(nr)         # 우선 순위가 높음
                else:             
                    visited[nr] = visited[r] + 1
                    Q.append(nr)   
        # print(r,visited)
    return 0            
                
N,K = map(int,input().split())
visited = defaultdict(int)
print(bfs())

