# https://www.acmicpc.net/problem/1715
#
'''
30 40 50 100
(30+40) 70, [50,70,100], cnt = 70
(50+70) 120, [100,120], cnt = 70 + 120
(100+120) 220,   cnt = 70 + 120 + 220 = 410

최소 몇 번의 비교가 필요한지 구하는 프로그램.
'''
import sys
from heapq import heappush,heappop
input = sys.stdin.readline

N = int(input())
card = []
ans = 0
cnt = 0
for i in range(N):
    heappush(card,int(input()))

while len(card) >= 2:
    cnt = heappop(card) + heappop(card)
    heappush(card, cnt )    
    ans += cnt
    # print(cnt,card)          
print(ans)    

'''
8
30
40
50
20
10
100
60
120

ans = 1160

8
30
40
50
20
10
100
60
10

ans = 860
'''