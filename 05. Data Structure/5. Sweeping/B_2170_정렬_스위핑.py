import sys
readline = sys.stdin.readline
N = int(readline())
data = [list(map(int,readline().split())) for _ in range(N)]

data.sort(key=lambda x:(x[0],x[1])) # 정렬

start,end = data[0][0] , data[0][1]
cnt = abs(end - start)  # x[0]가 x[1]보다 큰 경우에 대한 예외 처리

for i,x in enumerate(data):
    # x[0]가 x[1]보다 큰 경우에 대한 예외 처리
    if x[0] > x[1] :
        temp = x[0]
        x[0] = x[1]
        x[1] = temp         
        
    if start <= x[0] <= end and start <= x[1] <= end:   # x[0]와 x[1] 모두 start와 end 범위에 위치할때    
        continue
    elif start <= x[0] <= end:      # x[0]가 start와 end사이에 위치해 있지만, x[1]은 end보다 값이 클때
        cnt += x[1] - end
        end = x[1]
    else:                           # start와 end에도 속하지 않는 경우, 즉 동떨어진 경우
        start,end = x[0],x[1]       # 다시 star와 end를 정의
        cnt += end - start

print(cnt)

