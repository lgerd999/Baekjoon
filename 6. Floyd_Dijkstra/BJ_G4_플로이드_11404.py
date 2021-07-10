# https://www.acmicpc.net/problem/11404
'''
플로이드 마샬 알고리즘은 다익스트라 알고리즘과 같이 최단 경로를 구하는 데 사용되며, DP의 한 형태임
다익스트라가 한 경로에서 다른 경로까지의 최단경로를 구하는 경우라면, 플로이드 마샬 알고리즘은 모든 경로에 대해 최단 경로를 구한다는 특징이 있음
'''
import sys
INF = sys.maxsize
input = sys.stdin.readline  # 시간 초과 방지

# 플로이드 마샬 알고리즘 함수
def flolyd(dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
    return dist

n = int(input())      
bus = int(input())            

# 도시 사이 버스(경로)가 없으면 무한으로 표기
data = [[INF]*n for _ in range(n)]

# 노드가 자기 자신일 경우 0 임
for i in range(n):    
    data[i][i] = 0
            
for _ in range(bus):
    a,b,c = map(int,input().split())
    # 도시간 버스 노선이 겹치는 경우 최소가 되는 값을 택한다.
    if data[a-1][b-1] == INF:
        data[a-1][b-1] = c
    else:
        data[a-1][b-1] = min(data[a-1][b-1],c)     
#print(data)    

ans = flolyd(data)
for i in range(n):
    for j in range(n):
        # 문제에서 경로가 없는 경우 0으로 표기하게 함
        if ans[i][j] == INF:
            ans[i][j] = 0
    print(*ans[i],sep=' ')
        