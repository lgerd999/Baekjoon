# https://www.acmicpc.net/problem/2550
# LIS
'''
입력을 잘 봐야 하는 문제.
아래와 같이 입력이 들어왔다면, 2는 5번과 연결, 4는 1과 연결되어 있음을 파악해야 함(문제의 그림 참조)
2 4 1 5 3
4 5 1 3 2

스위치별로 정렬을 하게 되면, 연결되는 전구수가 틀어지는 문제가 발생하므로 정렬하지 않고 바로 사용해야 함.

'''

import sys
from bisect import bisect_left
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
switch = list(map(int,input().split()))
light = list(map(int,input().split()))

# 스위치와 전구가 같은 포트끼리만 연결되어 있으므로 connect라는 변수에 이의 인덱스를 저장.
connect = defaultdict(int)
for i in switch:
    connect[i] = light.index(i)+1

buf = [0]
# 리스트를 사용하지 않고 딕셔너리를 사용하였기 때문에 인덱스 문제가 발생한다. 이를 보정하기 위해 idx+1로 하였다.
dp = [0]*(N+1)  # 딕셔너리 사용으로 N+1개의 메모리가 필요.
connect_on = list(connect.keys())   # 리스트로 형변환하지 않으면 역추적시 dict_keys 에러 발생.
for idx,i in enumerate(connect_on) :
    if buf[-1] < connect[i]:
        buf.append(connect[i])
        dp[idx+1] = len(buf)-1
    else:
        dp[idx+1] = bisect_left(buf,connect[i])   
        buf[dp[idx+1]] = connect[i]
print(len(buf)-1)        

value = max(dp) + 1
result = []
for i in range(N,0,-1):
    if dp[i] == value -1:
        result.append(connect_on[i-1])  # connect_on은 리스트이기 때문에 i-1로 인덱스 조정이 필요.
        value = dp[i]        
# print(result)
print(' '.join(map(str,sorted(result))))        