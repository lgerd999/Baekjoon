# https://www.acmicpc.net/problem/1655

from heapq import heappush,heappop
import sys
input = sys.stdin.readline

Num = int(input())

Left = []
Right = []

for i in range(Num):
    N = int(input())           
                          
    if i % 2 == 0 : # 1,3,5... 개수는 2개, 4개, 6개... 이므로 i를 2로 나누면... i가 3이면 i/2 = 1.5 이므로                 
        heappush(Left,-N)  # 최대힙
    else:   # i가 4라고 하면, 개수는 5개이므로 i/2는 몫이 2인 위치가 중간.                
        heappush(Right,N)  # 최소힙     
       
    # 짝수개가 주어졌을 때 중간에 있는 두 수 중에서 작은 수를 말해야 함
    # 왼쪽의 첫번째 수가 중간 값인데, 오른쪽 힙보다 왼쪽 힙의 값이 더 큰 경우에 대해 처리 SWAP해 줘야 함
    if len(Left) > 0 and len(Right) > 0 and -Left[0] > Right[0]:  
        # 왼쪽과 오른쪽의 값을 교환
        max_value = -heappop(Left)  
        min_value = heappop(Right)
        
        heappush(Left, -min_value)
        heappush(Right,max_value)
            
    print( -Left[0])
    
    