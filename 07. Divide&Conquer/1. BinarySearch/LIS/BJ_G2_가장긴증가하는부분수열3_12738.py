# https://www.acmicpc.net/problem/12738
#
'''
가장 긴 증가하는 부분수열2 문제와의 차이점 : Ai의 범위가  -1,000,000,000 ≤ Ai ≤ 1,000,000,000
(음수 부분 고려)
--> buf의 초기값만 변경.

'''

import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
prog = list(map(int,input().split()))

buf = [-INF]
for i in prog:
    if buf[-1] < i:
        buf.append(i)
    else:
        start = 0
        end = len(buf)-1    
        #ans = 0
        while start <= end:
            mid = (start + end)//2
            if buf[mid] < i:
                start = mid +1
                #ans = mid
            else:
                end = mid - 1
        buf[start] = i                

print(len(buf)-1)
'''
1
-1000000000 
답 : 1
'''