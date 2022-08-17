# https://www.acmicpc.net/problem/1806
# 투포인트

'''

'''
import sys
input = sys.stdin.readline
INF = sys.maxsize

N,S = map(int,input().split())
E = list(map(int,input().split()))

buf = INF
total = 0
end = 0
for start in range(N):
    while total < S and end < N:
        total += E[end]
        end += 1

    if total >= S:
        buf = min(buf,end-start)        
    total -= E[start]

if buf == INF: # INF가 나왔다는 말은 S보다 큰 값이 없다는 것으로 0을 출력한다.  
    print(0)
elif buf == 0: #길이가 최소 1이다.
    print(1)    
else:                 
    print(buf)
'''
10 100
1 1 1 1 1 1 1 1 1 1
ans = 0

10 0
1 1 1 1 1 1 1 1 1 1
ans = 1

10 100
5 1 3 5 10 7 4 9 2 8
ans = 0

10 21
11 2 5 6 8 9 2 3 10 9 10
'''