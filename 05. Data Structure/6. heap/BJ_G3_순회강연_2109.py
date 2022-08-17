# https://www.acmicpc.net/problem/2109
#
'''
각 대학에서는 d일 안에 와서 강연을 해 주면 p만큼 강연료를 지불.
가장 많은 돈을 벌 수 있도록 순회 강연하려 한다.

조건1 하루에 최대한 한 곳에서만 강연할 수 있다.
예를 들어, 4개 대학에서 제시한 p가 50,10,20,30이고, d값이 2,1,2,1이라면,
(50,2)(10,1)(20,2)(30,1)
--> day로 정렬 (50,2)(20,2),(30,1)(10.1)
==> 1일 안에 와서 강연(10,30) : 4번 대학, 2일 안에 와서 강연(50,20): 1번 대학 에서 강연하면 최대 80만큼 돈을 벌 수 있다.

구현
1. d일 안에 와서 강연하면 되고 이 중에서 가장 많은 돈을 주는 곳을 선택하면 됨.
 --> d에 관해서 오름차순
 --> 최소힙을 이용해서 힙에 들어 있는 개수와 d를 비교해서 힙의 갯수가 많을 경우 가장 최소값을 힙에서 제거
 
'''
import sys
from heapq import heappush,heappop
input = sys.stdin.readline

n = int(input())
schedule = [list(map(int,input().split())) for _ in range(n)]
# d에 관해서 오름차순으로 정렬
S = sorted(schedule,key=lambda x: x[1])
print(S)

cost = []
for p,d in S:
    heappush(cost,p)
    # 현재 힙에 있는 갯수가 d보다 크다면 가장 작은 값을 제거한다.
    if (len(cost) > d):
        heappop(cost)

print(sum(cost))

'''
3
100 2
50 2
30 1

ans = 150

3
1 1
10 2
10 2

ans = 20

'''    