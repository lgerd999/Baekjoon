import sys
from collections import deque,defaultdict

input = sys.stdin.readline

def bfs():
    Q = deque()
    Q.append(S)
    visited = defaultdict(int)    
    
    while Q:
        r = Q.popleft()
        
        if r == T:
            while r != S:
                # print(r)
                result.append(visited[r][1])
                r = visited[r][0]                
            return result[::-1]    
                       
        for n in (r*r,r+r,r-r,r//r):        
            if 0 < n <= T and not visited[n]:                
                if n == r*r:
                    visited[n]=(r,'*')   
                elif n == r+r:
                    visited[n]=(r,'+')
                elif n == r-r:
                    visited[n]=(r,'-') 
                else:
                    visited[n]=(r,'/')    
                                        
                Q.append(n)
    return '-1'
S,T = map(int,input().split())
result = []

if S == T:
    print('0')
else:    
    print(''.join(map(str,bfs())))
