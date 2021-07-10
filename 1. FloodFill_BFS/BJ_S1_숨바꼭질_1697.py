# https://www.acmicpc.net/problem/1697
from collections import deque,defaultdict
def bfs():
    queue = deque()
    queue.append(N)
    
    while queue:
        r = queue.popleft()             
        if r == K:            
            return visited[r]

        for n in (r-1,r+1,r*2):
            if 0 <= n <= 100001 and not visited[n]:
                visited[n] = visited[r] + 1
                queue.append(n)      
        print(visited)            
    return 0

N,K = map(int,input().split())
visited = defaultdict(int)
print(bfs())
            
