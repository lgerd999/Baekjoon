# https://www.acmicpc.net/problem/16437

from collections import defaultdict,deque
import sys
input = sys.stdin.readline

def bfs():     
    visited = defaultdict(list)
    Q = []      
    Q.append([1,0])    
    ans = 0
    dist = defaultdict(int)
    while Q:
        v,w = Q.pop()
        if v is not dist:                
            dist[v] = w
            for a,b in enumerate(data[v]):     # 가중치, 노드
                visited[v].append(b[0])    # 리프 노드를 구할 수 있음                                
                alt = w + b[1]
                #if w < 0 :   # 늑대섬
                if alt > 0:   # 양이 더 많을 때
                    data[v][a][1] = 0 # 늑대들은 더 이상 양을 잡아 먹지 않는다.
                    #ans -= b[1]
                else :              # 늑대가 더 많을 때                        
                    data[v][a][1] += b[1]   
                    #ans = 0                        
                        
                #else:
                #     dist[v] = 0
                ans += alt
                #data[v][a][1] = 0
                Q.append((b[0],alt))
    print('***2=',data,sep='\n')
    print('***3=',dist,visited,sep='\n')
    return ans

data = defaultdict(list)
N = int(input())
visited = [0]*N
for i in range(1,N):    
    t,a,p = input().split()
    if t == 'S':        
        data[int(p)].append([i+1,int(a)])
    else:        
        data[int(p)].append([i+1,-int(a)])
leaf = set(range(1,N+1)) - set(data.keys())
print('***1=',data,leaf,sep='\n')
print(bfs())

'''
늑대는 지나갈때마다 잡아 먹는게 아니라 평생 최대 한마리만 잡아 먹음.
7
W 10 1
W 40 2
W 10 2
S 100 3
S 50 3
S 20 4
ans = 110
'''