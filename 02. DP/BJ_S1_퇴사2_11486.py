import sys
readline = sys.stdin.readline
N = int(readline())
data = [list(map(int,readline().split())) for _ in range(N)]
DP = [0] * (N+50)
ans = 0
for i in range(N,0,-1):    
    if (i+data[i-1][0]) > (N+1): # 퇴사 날짜를 넘어가는 경우
        DP[i] = DP[i+1]
    else :                       # 역순까지의 DP값과 현재 DP값 중 최대값을 선택
        DP[i] = max(DP[i+1],DP[i+data[i-1][0]] + data[i-1][1])
    if ans < DP[i]:
        ans = DP[i]            
print(ans)