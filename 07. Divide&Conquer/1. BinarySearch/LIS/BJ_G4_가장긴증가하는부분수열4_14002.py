import sys
input = sys.stdin.readline
N = int(input())
data = list(map(int,input().split()))
result = []
DP = [1]*N
cnt = 1
for i in range(N):
    for j in range(i):
        # 기존 데이터보다 크면 +1
        if data[i] > data[j]:
            # +1된 데이터 유지를 위해 max 함수 사용
            #DP[i] = max(DP[i],DP[j]+1)
            if DP[i] < DP[j]+1:
                DP[i] = DP[j]+1                
value = max(DP)
print(value)

for i in range(N-1,-1,-1):
    if DP[i] == value:
        result.append(data[i])
        value -= 1
result.reverse()         
print(*result)