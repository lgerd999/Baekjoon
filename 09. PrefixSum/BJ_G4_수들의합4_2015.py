# https://www.acmicpc.net/problem/2015
# 누적합
'''
N과 A[1],A[2],...,A[N]이 주어졌을 때 N*(N+1)//2개의 부분합 중 합이 K 인 것이 몇 개나 있는지 구하는 문제

예) 2 -2 2 -2의 부분합의 개수를 나열하면 다음과 같다. 
A[0],A[1],A[2],A[3]  <== 4개
A[0:1],A[0:2],A[0:3] <== 3개
A[1:2],A[1:3]        <== 2개
A[2:3]               <== 1개
==> n = 4, 4*(4+1)//2 = 10개

'''
import sys
from collections import defaultdict

input =sys.stdin.readline

N,K = map(int,input().split())
array = list(map(int,input().split()))

# 누적합
S = [0]*(N+1)
for i in range(1,N+1):
    S[i] = S[i-1] + array[i-1]
    
'''
부분합은 누적합의 형태로 표현 가능.
A[j] + ... + A[i] == S[i] - S[j-1]
S[i] - S[j-1] == K
S[j-1] = S[i]-K (j-1 < i)
'''
ans = 0
cnt = defaultdict(int)
cnt[0] = 1  # S[0] = 0이기 때문에 cnt[0]에 1을 추가
for i in range(1,N+1):
    ans += cnt[S[i]-K]  # j-1 찾기
    cnt[S[i]] += 1
    print(ans,cnt)
print(ans)      