# https://www.acmicpc.net/problem/12014
# LIS
'''
문제를 읽어보면 LIS 유형
'''
import sys
from bisect import bisect_left
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N,K = map(int,input().split())
    stock = list(map(int,input().split()))

    buf = [0]
    flag = False
    for i in stock:
        if buf[-1] < i:
            buf.append(i)
        else:
            buf[bisect_left(buf,i)] = i
        if len(buf[1:]) == K:
            print(buf)
            flag = True        
            break
    print("Case #"+str(t+1))
    if flag:        
        print('1')
    else:
        print('0')