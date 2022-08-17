# https://www.acmicpc.net/problem/1939
'''
'''
import sys
from collections import defaultdict,deque
from bisect import bisect_left
input = sys.stdin.readline

def bfs(mid):
    Q = deque()
    visited[start] = 1
    Q.append(start)

    while Q:
        node = Q.popleft()
        if node == end:
            return True
        for n,w in data[node]:
            # 
            if visited[n] == 0 and mid <= w:
                Q.append(n)
                visited[n] = 1
    #print(visited)
    return False            

N,M = map(int,input().split())  # N : node, M : edge
data = defaultdict(list)
for _ in range(M):
    a,b,c = map(int,input().split())
    data[a].append((b,c))
    data[b].append((a,c))

start, end = map(int,input().split())
low, high = 0, 1000000000
while low <= high:
    visited=[0 for _ in range(N+1)]
    mid = (low+high)//2
    possible = bfs(mid)
    print(mid,low,high,possible)
    if possible:
        low = mid +1
    else:
        high = mid -1    

print(high)

'''
5 5
1 2 5
2 3 4
1 3 3
1 4 3
4 5 1
5 1
ans: 1

6 9
1 2 7
1 3 8
1 4 7
1 6 9
2 3 7
3 4 7
3 5 7
4 5 7
4 6 7
6 3
ans: 8

6 12
1 2 7
1 3 8
1 4 7
1 6 9
2 3 7
3 4 7
3 5 7
4 5 7
4 6 7
3 6 7
1 3 11
5 6 12
6 3
ans: 9

3 1
1 2 999999999
1 2
ans: 999999999

3 3
1 2 2
3 1 2
2 3 2
1 3
ans: 2

3 3
1 2 2
3 1 2
2 3 99999999
1 3
ans: 2

'''



