# https://www.acmicpc.net/problem/2568
#
'''
전봇대 A와 B사이에 전기줄을 추가하다 보니 서로 교차하는 경우가 발생. 전기줄이 교차하지 않도록 
'''
import sys
from bisect import bisect_left
from collections import defaultdict
input = sys.stdin.readline

def lis(data):
    buf = [0]
    remove = set()
    dp =[0]*(N+1)
    for idx,i in enumerate(data):
        if buf[-1] < i:
            buf.append(i)
            dp[idx]=len(buf)-1
        else:
            dp[idx] = bisect_left(buf,i)
            buf[dp[idx]] = i
    # print(data)
    data = list(data)
           
    # 가장 큰 값부터 거슬러 올라가며 부분 수열을 찾는다.
    result = []
    value = max(dp)+1
    for i in range(N-1,-1,-1): # dp[N-1] ~ dp[0]
        if dp[i] == value-1:    # 가장 긴 증가하는 부분수열 길이가 최대. value = value -1 
            result.append(data[i])  # 그 때 data[i]에 있는 값 추가 
            value = dp[i]       # 제일 먼저 값이 같아지는 index 
    
    # print(buf,result)
    remove = set(data)-set(result)            
    return remove
    
    
N = int(input().rstrip())
data = [list(map(int,input().split())) for _ in range(N)]
data = sorted(data, key=lambda x: x[0])
pole = defaultdict(int)
for a,b in data:    
    pole[b] = a

ret = lis(pole.keys())
print(len(ret))
ans =[]
for i in ret:
    ans.append(pole[i])

for i in sorted(ans):
    print(i)    

'''
10
461172 179604
450010 52741
433823 483423
281069 492282
494933 325829
370116 463789
397772 84522
283770 375649
467088 487809
385495 279870

6
281069
385495
397772
450010
461172
494933
--------------

4
1 2
2 3
3 4
4 1

1
4
'''
