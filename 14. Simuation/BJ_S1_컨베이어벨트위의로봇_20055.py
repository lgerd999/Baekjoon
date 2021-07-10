# https://www.acmicpc.net/problem/20055

from collections import deque

N,K = map(int,input().split())      # N : 벨트 수, K = 내구도 0인 벨트 수
A = deque(map(int,input().split()))       # 컨베이어 벨트 내구도  
robot = deque([0] *2*N)    # 로봇 수

cnt = 1 # 단계 카운트

while True:
    # 1
    robot.rotate(1)
    A.rotate(1)
    robot[N-1] = 0 # 내리는 위치의 로봇은 내린다.
    #2
    for i in range(N-2,-1,-1):
        if robot[i] and not robot[i+1] and A[i+1]:    # 로봇 진행 방향에 로봇이 없고 현재 내구도가 0이 아니라면.
            robot[i+1], robot[i] =  robot[i],0
            A[i+1] -= 1    # 내구도 하나 줄인다.
    robot[N-1] = 0        
    #3  
    if not robot[0] and A[0]:    # 올리는 위치에 있는 벨트 칸의 내구도가 0이 아니면, 올리는 위치에 로봇을 올린다
        robot[0] = 1
        A[0] -= 1
    #4
    if A.count(0) >= K:  # 내구도가 0인 칸의 개수가 K개 이상이면 종료
        break
    cnt += 1
print(cnt)    