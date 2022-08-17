#
#
import sys
import math
from collections import deque

input = sys.stdin.readline

def prime_number():  #  2 ~ n 까지의 소수 구하기
    # 모든 수가 소수라고 가정하고 True로 값을 설정.(0과1은 제외)
    array = [True for i in range(10000)]
    array[0] = False
    array[1] = False
    # 2부터 n의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(10000)) +1):
        if array[i] == True:    # i가 소수인 경우
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i*j <= 9999:
                array[i*j] = 0
                j += 1
    return array

def bfs(start,end):
    visited = [0] * 10000
    Q = deque()
    Q.append((start,0))
    visited[start] = 1
    
    while Q:
        r,cnt = Q.popleft()
        node = str(r)
        if r == end:
            return cnt
        
        for n in range(4):            
            for i in range(10):
                tmp = int(node[:n]+str(i)+node[n+1:])
                # print(tmp)
                if not visited[tmp] and prime[tmp] and tmp > 999:
                    visited[tmp] = 1
                    Q.append((tmp,cnt+1))
            
    return -1    
        
prime = prime_number()        
  
T = int(input())
for _ in range(T):
    s,e = map(int,input().split())
    ans = bfs(s,e)
    if ans == -1:
        print('Impossible')
    else:
        print(ans)        

