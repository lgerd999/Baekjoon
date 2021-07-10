# https://www.acmicpc.net/problem/2447

def star(x, y, n):
   if n == 1:
       paper[x][y]='*'
       return
   k = n//3          
   star(x, y, k)
   star(x, y+k, k)
   star(x, y+k+k, k)
   star(x+k, y, k)
   star(x+k, y+k+k, k)
   star(x+k+k, y, k)
   star(x+k+k, y+k, k)
   star(x+k+k, y+k+k, k)

N=int(input())
paper = [[' 'for i in range(N)] for _ in range(N)]
star(0, 0, N)           
for i in range(N):
    print(*paper[i],sep='') 
