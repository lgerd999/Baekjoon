# https://www.acmicpc.net/problem/2512
# 이분 탐색.

import sys
input = sys.stdin.readline


N = int(input())
burget = sorted(list(map(int,input().split())))
M = int(input())

start = 0   # 최소 예산으로 시작하면 50%에서 틀림. 0부터 시작해야 함.
end = burget[-1]
ans = 0
while start <= end:
    mid = (start + end)//2
    total = 0
    for i in burget:        
        if i >= mid:                        
            total += mid
        else:
            total += i
    if total <= M :        
        ans = mid
        start = mid +1                            
    else:        
        end = mid -1
        
print(ans)            

'''
5
4 4 5 5 2
7
output: 0
correct answer: 1

3
3 2 4
5
output: 0
correct answer: 1

3
4 4 5
6
output: 0
correct answer: 2
'''