# https://www.acmicpc.net/problem/12015
#
'''
LIS(Longest Increasing Subsequence:가장 긴 증가하는 수열)
 -- 주어진 수열내에서 가장 긴 부분 수열 찾기
 -- LIS를 풀기 위해서는 DP 이용. 복잡도 O(n^2)\
     dp = [1]*n
     for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i],dp[j]+1)
     print(max(dp))           
 -- 시간 복잡도를 개선하기 위해 이분 탐색 방법을 이용. 복잡도 O(nlogn)
 
 
수열 A가 주어졌을 때, 가장 긴 부분 수열을 구하는 프로그램
예) A = {10,20,10,30,20,50} 이라면,
10 x
10 20 x
20 x
10 x
30 x
20 30 x
10 20 30 x
20 x
50
30 50
20 30 50
10 20 30 50


'''
import sys
input = sys.stdin.readline

N = int(input())
prog = list(map(int,input().split()))

'''
# DP를 이용한 방법 : 시간 초과
buf = [1]*N
for i in range(N):
    for j in range(i):
        if prog[i] > prog[j]:
            buf[i] = max(buf[i],buf[j]+1)
print(buf)        
print(max(buf))
'''
# 이분 탐색을 이용한 방법
buf = [0]
for i in prog:
    if buf[-1] < i:
        buf.append(i)
    else:
        '''
        예를 들어, buf에 10 20 40 60이 들어 있는데 i가 50이라고 한다면,
        60을 50으로 교체해야 한다. 이유는 i 다음에 오는 수가 55인 경우, 60 이라면 수열을 이어갈 수 없기 때문.
        이분탐색으로 50이 들어갈 자리를 찾는다.
        
        '''
        start = 0
        end = len(buf)-1            
        while start <= end:
            mid = (start + end)//2
            if buf[mid] < i:
                start = mid +1                
            else:
                end = mid - 1
        buf[start] = i                
        '''
        # bisect 를 이용한 방법
        buf[bisect_left(buf,i)] = i
        '''
print(buf)
print(len(buf)-1)
'''

'''