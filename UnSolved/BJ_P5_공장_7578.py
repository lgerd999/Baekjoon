# https://www.acmicpc.net/problem/7578
# https://www.acmicpc.net/problem/2550 와 유사문제이지만 N의 개수가 50배 많아 세그먼트 트리를 이용해야만 통과가능.

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
  