# https://www.acmicpc.net/problem/16909
#
'''
카드의 능력치 : [A,B,C]
[A,A],[A,B],[A,B,C]
[B,B],[B,C]
[C,C]

문제는 카드의 개수 N이 백만개, 카드수도 백만개가 주어질 수 있으므로 메모리/시간 최적화가 필요하다.

특이점
1. 자기 자신은 모두 0, 모든 구성원은 정렬 후 배열[-1]-배열[0]
2. 주어진 배열의 최대,최소가 포함되면 최대-최소값은 동일. 
3. 

예를 들어, 2 5 3 4 라면, 10가지 경우의 수
[2],[5],[3],[4] : 0
[2,5] : 3
[2,5,3] : 3
[2,5,3,4]  : 3
[5,3] : 2
[5,3,4] : 2
[3,4] :1

2,5,3,4
--> (2,5),(5,3),(3,4),(2,5,3),(5,3,4)
--> 스택 S. (2,5),(S[-1],3),(5,3),(S[-1],4),(3,4)
    S[-1] = (2,5) --> (2,5,3),(5,3) --> (2,5,3,4),(5,3,4)
    


'''

import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
ability  = list(map(int,input().split()))
'''
# 시간 초과 - 브로드포스
result = []
for i in range(N):    
    ans = []    
    for j in range(i,N):        
        ans.append(ability[j])        
        print(ans)
        result.append(max(ans)-min(ans))
print(sum(result))            
'''
ans = []
result = 0
for i in range(N):    
    
    if not ans:
        ans.append(ability[i])
    else:
        x = ans.pop()
        if  x > ability[i]:
            max_value = x        
            min_value = ability[i]    
        else:    
            max_value = ability[i]            
            min_value = x        
        result = max_value - min_value
        ans.append(ability[i])            
        ability.append(result)
    print(ans,ability)    
    
'''
4
2 5 3 4


'''    