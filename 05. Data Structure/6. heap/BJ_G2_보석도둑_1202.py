# https://www.acmicpc.net/problem/1202
#
'''
총 보석 : N
보석 무게와 가격 : M_i, V_i
가방 : K
각 가방에 담을 수 있는 최대 무게 : C_i

조건 : 가방에는 최대 한 개의 보석만 넣을 수 있다.

보석의 최대 가격을 구하는 프로그램.

예) N = 2, K = 1
1번 보석 : 무게-5, 가격-10
2번 보석 : 무게-100, 가격-100
가방에 담을 수 있는 최대 무게 : 11
================================
답 :  가방 1개에 1번 보석만 담을 수 있다.

예) N = 3, K = 2
보석 : (1,65),(5,23),(2,99)
가방 무게 : (10,2)
----------------------------
==> 정렬 : (2,99),(1,65),(5,23) - 가격에 따른 정렬()
==> 여기서 가방에 담을 수 있는 보석을 저장 :(2,99),(1,65) - 무게에 따른 정렬 필요
==> 
가방1(10) : 99
가방2(2) : 65
'''

import sys
from heapq import heappush,heappop
input = sys.stdin.readline

N,K = map(int,input().split())

# 보석의 무게 및 가격에 대해 2가지 방식으로 입력 받을 수 있다.
# 1. 일반적인 입력
# jewel = [list(map(int,input().split())) for _ in range(N)]
# 2. 힙으로 입력(가장 작은 무게가 첫번째 배열로 정렬됨)
jewel = []
for _ in range(N):
    heappush(jewel,list(map(int,input().split())))

# 가방이 가지는 최대 무게 입력 후 오름차순 정렬    
weight = [int(input()) for _ in range(K)]
weight.sort()

# print(jewel,weight)

bag = []
price = 0
for w in weight:
    while jewel and w >= jewel[0][0]:   # 가방의 한도 무게와 보석의 무게 비교        
        # heappush(bag,-jewel[0][1]) # 보석의 가격을 최대힙을 이용하여 bag에 다시 넣기
        # heappop(jewel)
        heappush(bag,-heappop(jewel)[1]) # 보석의 가격을 최대힙을 이용하여 bag에 다시 넣으면 가장 큰 음수가 제일 앞으로 정렬됨

    # print(bag,jewel)
    
    if bag:
        price -= heappop(bag)   # 가장 높은 보석의 가격 계산(최대힙을 사용하였기 때문에 -부호로 보정)
    elif not jewel: # 남은 보석이 없는 경우.
        break

print(price)        
    
        
            
                 
