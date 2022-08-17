# https://www.acmicpc.net/problem/12852
#
'''
정수 X에 대한 연산은 다음 세가지 이다.
1. X%3 == 0, X//3
2. X%2 == 0, X//2
3. X -= 1

예) 10
cnt = 1 : 10, 3번 연산 수행, X = 9
cnt = 2 : 9, 1번 연산, X = 3
cnt = 3, 3, 1번 연산, X = 1
==================================
총 3회, 10 9 3 1

'''
import sys
from collections import deque,defaultdict
input = sys.stdin.readline


def bfs():    
    Q = deque()
    Q.append(X)    
    visited[X] = -1
        
    while len(Q) >0:
        r = Q.popleft()
        # print(r)
        if r == 1:
            while r != X:
                result.append(visited[r])
                r = visited[r]
            print(len(result)-1)
            print(' '.join(map(str,result[::-1])))
            return                       
        
        if r%3 == 0 and not visited[r//3] :                                            
            Q.append(r//3)     
            visited[r//3] = r
            
            
        if r%2  == 0 and not visited[r//2]:                                  
            Q.append(r//2)     
            visited[r//2] = r
            
                        
        if not visited[r-1]:                                            
            Q.append(r-1)     
            visited[r-1] = r
            
                                                                   
                
X = int(input())    
result = [1]
visited = defaultdict(int)   
bfs()
