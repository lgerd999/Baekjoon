# https://www.acmicpc.net/problem/11780
# 참조 : https://zoosso.tistory.com/378
#       https://www.youtube.com/watch?v=hw-SvAR3Zqg
'''
경로를 출력해야 하므로, 입력에 사용된 값을 index로 바로 사용할 수 있도록 1~n+1까지 배열을 잡는다.

* 출력에 대한 설명
1. 도시의 개수 도시i 도시j : 도시 i에서 j로 갈때 가장 최소 비용으로 갈 수 있는 경우만 출력
 - 3 1 3 5 : 도시1에서 도시 5까지 가는 경로 중 가장 최소 비용으로 갈 수 있는 경우는 도시 1번에서 3번을 거쳐 5번으로 가능 경우이므로 도시 개수는 3
 - 도시 i에서 j로 가능 경로가 없는 경우 0 출력(자기 자신)
 아래와 같이 모든 도시에 대해서 가장 최소 비용으로 목적지까지 가는 경로를 출력하는 문제임
 (1,2)(1,3)(1,4)(1,5)
 (2,1) ...
 (3,1) ... 
 (4,1) ...
 (5,1)(5,2)(5,3)(5,4)

'''
import sys
INF = sys.maxsize
input = sys.stdin.readline  # 시간 초과 방지

# 최소 비용 경로를 구하는 재귀함수
def find_path(i, j):
    if trace[i][j] == 0:
        return []

    k = trace[i][j]
    '''
    1. find_path[i][j]는 trace[i][j] = 0이면 return하고 값이 있다면 2번수행
    2. k값은 정해지고 find_path(i,k)계산해서 값이 0이면 return하고 있으면 find_path(j,k)위치에 k값 반영
    3. find_path[k][j]도 2번과 같이 수행
    '''
    return find_path(i, k) + [k] + find_path(k, j)

# 플로이드 마샬 알고리즘 함수
def flolyd(dist):
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    trace[i][j] = k # 도시 i,j로 이동에 따른 최소 비용 계산을 위한 k값 저장
    print('k=',trace)
    return dist

n = int(input())      
bus = int(input())            

# 도시 사이 버스(경로)가 없으면 무한으로 표기
data = [[INF]*(n+1) for _ in range(n+1)]

# 경로 추적을 위해 k를 저장할 변수 정의
trace = [[0]*(n+1) for _ in range(n+1)]

# 노드가 자기 자신일 경우 0 임
for i in range(1,n+1):    
    data[i][i] = 0
            
for _ in range(bus):
    a,b,c = map(int,input().split())
    # 도시간 버스 노선이 겹치는 경우 최소가 되는 값을 택한다.
    if data[a][b] == INF:
        data[a][b] = c
    else:
        data[a][b] = min(data[a][b],c)     
#print(data)    

ans = flolyd(data)
for i in range(1,n+1):
    for j in range(1,n+1):
        # 문제에서 경로가 없는 경우 0으로 표기하게 함
        print(ans[i][j] if ans[i][j] != INF else 0, end=' ')        
    print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            print(0)
            continue        
        print(find_path(i,j),i,j)
        path = [i] + find_path(i,j) + [j]
        print(len(path), end=' ')
        print(*path)
