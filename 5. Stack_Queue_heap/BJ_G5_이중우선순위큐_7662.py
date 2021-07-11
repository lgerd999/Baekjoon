# https://www.acmicpc.net/problem/7662

from heapq import heappush,heappop
from collections import defaultdict
import sys
input = sys.stdin.readline

def sync(arr):
    while arr and marked[arr[0][1]] == 0:
        heappop(arr)

T = int(input())
for _ in range(T):
    k = int(input())
    min_Q = []
    max_Q = []
    marked = defaultdict(int)
    for i in range(k):
        c,n = input().split()        
        if c == 'D':
            if n == '1':
                sync(max_Q)
                if max_Q:
                    marked[max_Q[0][1]] = 0     # heapq의 첫번째 값의 1번째 인자값에 대해 0으로 설정
                    heappop(max_Q)
            elif n == '-1':
                sync(min_Q)
                if min_Q:
                    marked[min_Q[0][1]] = 0     # heapq의 첫번째 값의 1번째 인자값에 대해 0으로 설정
                    heappop(min_Q)

        elif c == 'I':
            heappush(min_Q,(int(n),i))        
            heappush(max_Q,(-int(n),i))
            marked[i] = 1
    # for문 완료 후 최종 sync         
    sync(min_Q)
    sync(max_Q)

    print(min_Q,max_Q)
    if not min_Q or not max_Q:  # sync가 정확히 되었다면 큐가 빌 때 min과 max 큐가 모두 비어야 함
        print('EMPTY')
    else:
        print(-max_Q[0][0],min_Q[0][0])


'''
1
7
I 5
I 3
I 7
I 6
D 1
D -1
D -1
ans = 6 6
'''
            
