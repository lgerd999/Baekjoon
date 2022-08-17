# https://www.acmicpc.net/problem/5014
# BFS 문제
'''
건물 : 총 F층 , 스타트 링크 위치 : G층
강호 위치 : S, 엘리베이터 : S -> G
엘리베이터 : U(위), D(아래)층 갈 수 있는 버튼만 존재
(즉, U층만큼 위로 이동하거나 D층만큼 아래로 이동할 수 있음)
엘리베이터로 이동할 수 없는 경우 "use the starirs" 출력

F,S,G,U,D 가 입력으로 주어짐.
강호가 S -> G 층으로 가기 위해 눌러야 하는 버튼의 수 최소값

'''

import sys
from collections import deque

input = sys.stdin.readline

def bfs():

    Q = deque()
    Q.append((S,0))
    visited[S] = 1
    cnt = 0
    while Q:
        # s : 강호 위치 
        s,cnt = Q.popleft()
        # print(s,cnt)
        if s == G:
            return cnt     
        for n in (s+U, s-D):
            if 0 < n <= F:
                if not visited[n]:
                    visited[n] = 1
                    Q.append((n,cnt+1))
    return -1


F,S,G,U,D = map(int,input().split())
visited = [0]*(F+1)
ans = bfs()
if ans == -1:
    print("use the stairs")
else:
    print(ans)    

'''
총 10층 건물, 강호는 1층에 있고, 스타트링크는 10층 위치, 엘레베이터는 2층과 1층 버튼만 있음.
10 1 10 2 1
6

100 2 1 1 0
use the stairs
'''