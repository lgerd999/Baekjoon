# https://www.acmicpc.net/problem/13458
N = int(input()) # 총 시험장 수
A = list(map(int,input().split())) # 시험장 당 응시생 수
B,C = map(int,input().split())  # 총감독관 및 부감독관이 감시할 수 있는 인원 수
#print(A,B,C)

sum = 0
for i in range(N):    
    if A[i] > B:
        cnt = 1
        Q,R = divmod(A[i] - B,C)
        if Q:
            cnt += Q
        if R:
            cnt += 1
    else:
        cnt = 1 # 시험장당 총감독관이 감시할 수 있는 인원 이하 인 경우            
    sum += cnt    
print(sum)                
