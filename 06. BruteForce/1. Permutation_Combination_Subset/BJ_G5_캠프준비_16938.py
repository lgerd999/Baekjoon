# https://www.acmicpc.net/problem/16938
#
'''
문제 수 : N, i 번째 문제의 난이도 : A_i
문제 난이도의 합은 L보다 크거나 같고, R보다는 작거나 같다.
가장 어려운 문제와 가장 쉬운 문제의 난이도 차이는 X보다 크거나 같다.
캠프에 사용도리 문제는 두 문제 이상.
캠프에 사용할 문제를 고르는 방법의 수를 구하기.

예) N : 3, L = 5, R = 6, X = 1
A_i = 1 2 3
-- 조건1 : 난이도 합이 L = 5 보다는 크거나 같고 R = 6 보다는 작거나 같아야 함
-- 조건2 : 가장 어려운 난이도 - 가장 쉬운 난이도 = X = 1
==> 정답 : (2,3),(1,2,3) - 2가지 방법

'''

import sys
from itertools import combinations
input = sys.stdin.readline

N,L,R,X = map(int,input().split())
A = list(map(int,input().split()))

cnt = 0
for i in range(1,N+1):
    for c in combinations(A,i):
        if L <= sum(c) <= R:
            if max(c) - min(c) >= X:
                cnt += 1
print(cnt)                