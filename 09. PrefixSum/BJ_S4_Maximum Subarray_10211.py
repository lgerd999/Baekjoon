# https://www.acmicpc.net/problem/10211
# 최대 부분배열 문제(Maximum Subarray Problem)
import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    array = list(map(int,input().split()))
    # dp = array
    dp = [i for i in array]
    '''
    dp = [0]*N
    dp[0] = array[0]
    '''
    # 이전 값과 현재값(누적합), 현재 값 중 최대값을 dp[i]에 저장
    for i in range(1, N):
        dp[i] = max(dp[i-1]+array[i], array[i])
    print(max(dp))