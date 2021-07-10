# https://www.acmicpc.net/problem/5585

pay = int(input())
coins = [500,100,50,10,5,1]
N = 1000 - pay
cnt = 0
for i in range(6):
    Q = N // coins[i]
    N -= Q*coins[i]    
    cnt += Q
print(cnt) 

