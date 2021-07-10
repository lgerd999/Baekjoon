#https://www.acmicpc.net/problem/1931

# N = int(input())
# data = [list(map(int,input().split())) for _ in range(N)]
# print(data)
N = 11
data = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]

data.sort(key=lambda x:(x[1],x[0])) #회의 시작시간과 종료 시간이 같을 수 있는 경우 시작시간이 먼저 인 것으로 처리하기 위해 x[0] 옵션 필요
print(data)
last = 0
cnt = 0
for start,end in data:
    if start >= last:
        last = end
        cnt += 1
print(cnt)        

