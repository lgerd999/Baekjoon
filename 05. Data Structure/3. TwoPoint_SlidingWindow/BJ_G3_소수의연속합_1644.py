# https://www.acmicpc.net/problem/1644
# 에라토스테네스의 체 알고리즘 + 투 포인트(배열의 특정 연속된 구간을 처리하는 경우 고려)

import sys
import math
input = sys.stdin.readline

N = int(input())
'''
# 소수 배열을 딕셔너리로 했을 때 메모리 초과 발생. pypy로는 통과됨.
arrary = {i:True for i in range(N+1)}
for i in range(int(math.sqrt(N))+1):
    if i < 2:            
        del arrary[i]
    if arrary.get(i):
        j = 2
        while i*j <= N:                
            if arrary.get(i*j):
                del arrary[i*j]
            j += 1    
'''
# 리스트로 변경시 메모리가 5배정도 감소되고 시간은 2배로 늘어남.
array = [True for i in range(N+1)]

# 2부터 n의 제곱근까지의 모든 수를 확인하며
for i in range(2, int(math.sqrt(N)) +1):
    if array[i] == True:    # i가 소수인 경우
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i*j <= N:
            array[i*j] = 0
            j += 1
pn = []
for i in range(2,N+1):
    if array[i]:
        pn.append(i)

# 투 포인트 방식으로 접근.
hap = 0
end = 0
cnt = 0
for start in range(len(pn)):
    while hap < N and end < len(pn):
        hap += pn[end]
        end += 1
    if hap == N:        
        cnt += 1
    hap -= pn[start]    

print(cnt)    
