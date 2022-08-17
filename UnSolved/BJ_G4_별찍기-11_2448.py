# https://www.acmicpc.net/problem/2448
# 참고1 : https://ssu-gongdoli.tistory.com/79
# 참고2 :  https://blog.naver.com/PostView.nhn?blogId=repeater1384&logNo=222090337859
'''
N은 3 x 2^k (3,6,12,24, 48,...)
=> N = 24, 세로 3 x 2^k  X 가로 6 x 2^k , k = 3
=> 가로 4등분, 세로 2등분하면 아래와 같이 나열할 수 있다.

(x        ,y)     (x        ,y+3*2^k-1)     (x        ,y+6*2^k-1)     (x        ,y+9*2^k-1)     (x        ,y+12^k-1)

(x+3*2^k-1,y)     (x+3*2^k-1,y+3*2^k-1)     (x+3*2^k-1,y+6*2^k-1)     (x+3*2^k-1,y+9*2^k-1)     (x+3*2^k-1,y+12^k-1)

(x+3*2^k  ,y)     (x+3*2^k  ,y+3*2^k-1)     (x+3*2^k  ,y+6*2^k-1)     (x+3*2^k  ,y+9*2^k-1)     (x+3*2^k  ,y+12^k-1)     

=> t = 2^(k-1)

(x   ,y)     (x   ,y+3t)     (x   ,y+6t)     (x   ,y+9t)     (x   ,y+12t)

(x+3t,y)     (x+3t,y+3t)     (x+3t,y+6t)     (x+3t,y+9t)     (x+3t,y+12t)

(x+6t,y)     (x+6t,y+3t)     (x+6t,y+6t)     (x+6t,y+9t)     (x+6t,y+12t)     


'''
import sys
sys.setrecursionlimit(10**6)

def star(x, y, n):
   if n == 1:
       paper[x][y]='*'
       return
   k = n//3  
   t = 2**(k-1)     
#    star(x, y, k)
#    star(x, y+k, k)
   star(x, y+6*t, k)
#    star(x, y+k+k+k, k)
#    star(x, y+k+k+k+k, k)
#    star(x, y+k+k+k+k+k, k)
   
#    star(x+k, y, k)
   star(x+3*t, y+3*t, k)
#    star(x+k, y+k+k, k)
   star(x+3*t, y+9*t, k)
#    star(x+k, y+k+k+k+k, k)
#    star(x+k, y+k+k+k+k+k, k)

   star(x+6*t, y, k)   
   star(x+6*t, y+3*t, k)
   star(x+6*t, y+6*t, k)   
   star(x+6*t, y+9*t, k)   
   star(x+6*t, y+12*t, k)
   

N=int(input())
paper = [[' 'for i in range(N)] for _ in range(N)]
star(0, 0, N)           
for i in range(N):
    print(*paper[i],sep='') 