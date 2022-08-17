# https://www.acmicpc.net/problem/2447

'''
N 이 3의 거듭제곱, NxN 정사각형 모양.
크기 3(3^1)의 패턴은 아래와 같음

***
* *
***
N이 3보다 클 경우, N 패턴은 공백으로 채워진 가운데 (N/3) x (N/3) 정사각형을 크기 N/3 패턴으로 둘러싼 형태

'''


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
