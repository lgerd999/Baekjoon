# https://www.acmicpc.net/problem/7576

from collections import deque

# N,M = map(int,input().split())
# data = [list(map(int,input().split())) for _ in range(M)]     
# print(data)    

N,M = 6,4
data = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]]

rr = [-1,1,0,0]
cc = [0,0,-1,1]

queue = deque()

cnt = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 1: # 익은 토마토를 큐에 저장
            queue.append([i,j])

while queue:
    for _ in range(len(queue)):
        r,c = queue.popleft()        
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]            
            if nr < 0 or nc < 0 or nr >=len(data) or nc >= len(data[0]):
                continue

            if data[nr][nc] == 0: # 인접한 토마토가 아직 익지 않았다면,
                data[nr][nc] = 1   # 익은 토마토로 저장
                queue.append([nr,nc]) # 익은 토마토 위치를 큐에 저장               
    cnt += 1  # 날짜 카운트

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 0: # 익지 않은 토마토가 있다면 날짜 카운트 리셋
            cnt = 0

print(cnt-1)            