import sys
readline = sys.stdin.readline
N = int(readline())
data = [list(map(int,readline().split())) for _ in range(N)]

data.sort(key=lambda x:(x[0],x[1]))
start,end = data[0][0] , data[0][1]
cnt = end - start
for i,x in enumerate(data):
    # 기존 선분에 겹치는 경우
    if start <= x[0] <= end and start <= x[1] <= end:                
        continue
    elif start <= x[0] <= end:
        cnt += x[1] - end
        end = x[1]
    else:        
        start,end = x[0],x[1] 
    if i+1 == N:        
        cnt += end - start

   
#cnt += end - start
print(cnt)

