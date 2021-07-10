#https://www.acmicpc.net/problem/4811

'''
N개의 알약이 든 병이 있고, 하루에 반 개의 알약만 먹고 나머지는 다시 병에 담는다.
약을 병에서 꺼낼 때 반개짜리 약을 꺼낼 때 'H', 쪼개지 않은 알약을 꺼낼 때 'W'를 손녀에게 문자로 전달한다.
N = 1 일 때, WH
N = 2 일 때, WHWH, WWHH
N = 3 일 때, WH WHWH/WH WWHH(앞에 알약 1개 소비하면 나머지는 N=2와 동일), 
             WW HWHH/WW HHWH(앞에 알약 2개는 N=2와 동일), 
             WWW HHH (앞에 알약 3개 연이어 먹는 경우의 수는 1개)

DP[1] = DP[0]
DP[2] = DP[1]xDP[0] + DP[0]xDP[1]
DP[3] = DP[2]xDP[0] + DP[1]xDP[1] + DP[0]xDP[2]

'''

dp = [0]*31
dp[0] = 1

for i in range(1,31):
    cnt = 0
    for j in range(i):
        cnt += dp[j]*dp[i-j-1]
    dp[i] = cnt

result = []
while True:
    N = int(input())
    if not N:
        break
    result.append(dp[N])    
print(*result,sep='\n')    