# https://www.acmicpc.net/problem/1849
#
'''
1부터 N까지 수들이 한번씩 쓰인 수열이 있다.(중복 X)
그 수열에서 i 보다 큰 수들의 개수를 A[i]. A[i]가 주어져 있을 때, 원래 수열 구하기.
예) 
i    = 1 2 3 4 5 6 7 8 
A[i] = 5 0 1 2 1 2 0 0
==> 1 앞에는 5개의 큰 수가 있고
i =  1 2 3 4 5 6 7 8 
               1        : 6
==> 2 앞에는 큰 수가 없다.
i =  1 2 3 4 5 6 7 8 
     2         1        : 1              
==> 3 앞에는 큰 수가 1개 있다.
i =  1 2 3 4 5 6 7 8 
     2   3     1                    
==> 4 앞에는 큰 수가 2개 있다.
i =  1 2 3 4 5 6 7 8 
     2   3   4 1                    
==> 5 앞에는 큰 수가 1개 있다.
i =  1 2 3 4 5 6 7 8 
     2   3 5 4 1                         
==> 6 앞에는 큰 수가 2개 있다.
i =  1 2 3 4 5 6 7 8 
     2   3 5 4 1   6                           
==> 7과 8 앞에는 큰 수가 없다다.
i =  1 2 3 4 5 6 7 8 
     2 7 3 5 4 1 8 6                                
             
'''

import sys
from bisect import bisect_left
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
dp = [-1]*(N+1)
buf = []
idx = 0
for i in range(1,N+1):
    eq = int(input())
    '''
    # 시간초과
    index = 0
    while eq > 0 :        
        if dp[index] > -1:
            pass
        else:
            eq -= 1    
        index += 1    
    if dp[index] == -1:        
        dp[index] = i        
    else:
        index += 1
        while dp[index] != -1:
            index += 1
        
        dp[index] = i
    
print('\n'.join(map(str,dp)))
''' 
    
    idx = bisect_left(dp,-1,0,eq+idx)
    buf.append(idx)
    
        
    # while dp[idx] != -1:
    #     idx += 1 
    # dp[idx] = i    
    # buf[i] = idx
    # print(idx,dp,buf.values())
    dp[idx] = i
    print('idx=',idx,dp)
    '''
    8
5
0
1
2
1
2
0
0
    '''