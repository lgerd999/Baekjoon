# https://www.acmicpc.net/problem/16933
# 참조 : https://velog.io/@evelyn82ny/boj-16933


'''
# 시간 초과를 피하기 위해서 
1. 배열이 3차면 pypy로 진행해야 하고, 4차를 고려하면 100% 시간초과됨.
2. queue를 고려해야 할 변수 갯수로 늘려서 적용하는 방법을 추천(아래 예시와 같이 사용)


# 이해하기 쉬운 정답
from collections import deque
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
matrix = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[sys.maxsize]*M for _ in range(N)]
dx,dy = [1,-1,0,0],[0,0,1,-1]

def bfs():
    queue = deque()
    queue.append((0,0,0,1,True))
    visited[0][0] = 0
    while queue:
        # wall : 벽 뚫기 횟수, step: 이동 거리, possible : 낮/밤
        x,y,wall,step,possible = queue.popleft()
        if x==N-1 and y==M-1:
            print(step)
            return
        for i in range(4):
            nx,ny =x+dx[i],y+dy[i]            
            if 0<=nx<N and 0<=ny<M:
                # 벽이 없고, visited가 벽 뚫기 횟수 보다 크면, 
                if matrix[nx][ny] == 0 and visited[nx][ny] > wall:
                    visited[nx][ny] = wall
                    queue.append((nx,ny,wall,step+1,not possible))
                # 벽이 있고, 벽 뚫기 횟수가 K보다는 작고     
                elif matrix[nx][ny] == 1 and visited[nx][ny] > wall+1 and wall<K:
                    if possible:
                        visited[nx][ny] = wall+1
                        queue.append((nx,ny,wall+1,step+1,not possible))
                    else:
                        queue.append((x,y,wall,step+1,not possible))
    print(-1)
    return
bfs()

'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    rr = [1,-1,0,0]
    cc = [0,0,1,-1]
    
    visited = [[K+1] * (M) for _ in range(N)]  # 해당 지점까지 오면서 벽을 부순 횟수 저장

    # 경로는 시작하는 칸과 끝나는 칸도 포함해서 센다.
    visited[0][0] = 0
    Q = deque()
    Q.append([0,0,0,1,1]) 
    
    # day = 1     # day가 1이면 낮. 시작점에서는 낮에 시작
    while Q:
        # 아래 for문은 이해가 안됨. 구글링해보면 같은 시점에 처리하기 위해서라고 되어 있음.
        # for _ in range(len(Q)):
        # d 는 이동거리, w는 벽을 뚫는 횟수
        r,c,w,dist,day = Q.popleft()        

        if r == N - 1 and c == M - 1:                            
            return dist     
                
        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]     
            nw = w + 1
            nd = dist + 1          
                            
            if nr < 0 or nc < 0 or nr >= N or nc >= M or w > K: #or visited[nr][nc]:
                continue             
                
            # 벽을 만나 벽을 뚫는 상황
            # nw = w+1 이는 벽을 하나 부수었기 때문에 +1을 해줌.
            if data[nr][nc] == '1' and w < K and visited[nr][nc] > nw:                           
                if day: # 낮이면 벽을 뚫고 이동거리와 벽을 부순 횟수를 증가시킨다.
                    visited[nr][nc] = nw
                    Q.append([nr,nc,nw,nd,1-day])                
                else:      # 밤인 경우 이동거리만 증가시키고 제자리에 있는다.                        
                    Q.append([r,c,w,nd,1-day])                    
                
            # 벽을 만나지 않은 상황    
            # 탐색하고자 하는 지점까지 오는 경로에서 벽을 부순 횟수 visited[nr][nc] 보다 현재 경로에서 벽을 부순 횟수 w가 더 적다면
            # 현재 경로를 통해 벽을 부수는 더 작은 횟수로 탐색.
            if data[nr][nc] == '0' and visited[nr][nc] > w:                    
                visited[nr][nc] = w
                Q.append([nr,nc,w,nd,1-day])           
        # day = 1 -day                        
    return -1
    

N,M,K = map(int,input().split())
data = [list(input()) for _ in range(N)]

# print(data)
print(bfs())
'''
2 4 2
0111
0110

ans = 7
'''