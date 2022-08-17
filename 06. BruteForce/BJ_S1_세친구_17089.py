# https://www.acmicpc.net/problem/17089
#
'''
N명의 사람이 있고, 여기서 세 사람 A,B,C를 고르려고 한다. 그리고 모두 친구여야 한다.
A의 친구 수 + B의 친구 수 + C의 친구 수가 최소가 되어야 한다.
친구의 수의 합을 계산할 때 세 사람은 빼고 계산해야 한다.
-조건1- A의 친구 수를 계산할 때, B와 C는 빼고 계산해야 하고
-조건2- B의 친구 수를 계산할 때, A와 C
-조건3- C의 친구 수를 계산할 때, A와 B

예) 5 6
1 2
1 3
2 3
2 4
3 4
4 5
-----
graph {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3, 5], 5: [4]}
graph.keys()에서 A를 정하고, graph[A]에서 B를 찾고, graph[B]이면서 graph[A]에서 C를 찾는다.

'''
import sys
from collections import defaultdict
input = sys.stdin.readline


N,M = map(int,input().split())
friend = [list(map(int,input().split())) for i in range(M)]

# print(friend)
graph = defaultdict(list)
for i,j in friend:
    graph[i].append(j)
    graph[j].append(i)

# print(graph)    

ans = M # A,B,C의 친구인 경우 세 친구의 수의 합의 최대는 M-6.
# A를 정하고, B는 A의 친구 중 한명이고, C는 B의 친구이며 동시에 A의 친구인 경우 찾기
for A in graph.keys():
    for B in graph[A]:
        for C in graph[B]:
            if C in graph[A]:
                # 조건1,조건2,조건3 각각 2개씩 빼줘야 함
                ans = min(ans,len(graph[A])+len(graph[B])+len(graph[C])-6)

if ans < M:
    print(ans)
else:
    print(-1)    
                