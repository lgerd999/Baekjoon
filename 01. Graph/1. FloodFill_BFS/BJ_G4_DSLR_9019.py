#  https://www.acmicpc.net/problem/9019
#

import sys
from collections import deque,defaultdict
input = sys.stdin.readline

def bfs(num):
    visited = defaultdict(int)
    Q = deque()
    Q.append((num,''))    
    visited[num] = 1
    while Q:        
        r,w = Q.popleft()        
        if r == B:
            return w
        
        for n in ('D','S','L','R'):                  
            if n == 'D':                
                nr= (2*r)%10000
            elif n == 'S':
                if r-1 < 0:
                    nr = 9999
                else:
                    nr = r -1    
            elif n == 'L':                
                nr = (r%1000)*10 + r//1000
            elif n == 'R':                                
                nr = (r%10) * 1000 + r//10
            if not visited[nr]:
                visited[nr] = 1                
                Q.append((nr,w+n))    
                               

T = int(input())

for _ in range(T):
    A = deque()
    A,B = map(int,input().split())
    print(bfs(A))

    
    