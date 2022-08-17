
# G1 https://www.acmicpc.net/problem/2718
# 참조 : http://joonas-yoon.blogspot.com/2016/03/2718.html

N = int(input())
DP = [0]*(N+1)

DP[0:2] = [1,1,5]
summ = 0
for i in range(3,N+1):
    summ += DP[i-3]
    DP[i] = 4*DP[i-2] + DP[i-1] + 2*summ
print(DP)