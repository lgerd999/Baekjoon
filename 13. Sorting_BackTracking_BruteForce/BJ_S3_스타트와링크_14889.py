# https://www.acmicpc.net/problem/14889

from itertools import combinations
import sys

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
'''
구현 아이디어(브루트 포스) - 조합과 집합을 이용하여 구현
1. Combination C는 Star,Link팀을 구성하기 위해 1~N 조합 중 N//2인 조합을 구성
2. Combination D는 팀 능력을 구하기 위해 각 C의 조합 중 2개인 조합을 다시 구함.
3. 집합을 사용하여 C 조합중에서 값이 중복되지 않도록 Star와 Link 팀을 구성.

'''
C = list(set(combinations(range(1,N+1),N//2)))
D = list(combinations(range(1,(N//2)+1),2))

# 해당 구현은 pypy에서만 패스가 되고 python에서는 시간 초과됨.
ans = sys.maxsize
for c in C:
    Star = set(c)
    Link = list(set(range(1,N+1))-Star) # 
    Star = list(Star)
    S_team,L_team = 0,0
    for i,j in D:
        S_team += data[Star[i-1]-1][Star[j-1]-1] + data[Star[j-1]-1][Star[i-1]-1]        
        L_team += data[Link[i-1]-1][Link[j-1]-1] + data[Link[j-1]-1][Link[i-1]-1]
    diff = abs(S_team - L_team)
    ans = min(ans,diff)
#    print(S_team,L_team)
print(ans)        

    
