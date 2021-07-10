# https://www.acmicpc.net/problem/1992

def quad_tree(x,y,n):
    global result
    color = data[y][x]
    double_break = False

    for i in range(x,x+n):
        if double_break: break
        for j in range(y,y+n):
            if data[j][i] != color:
                result +='('
                quad_tree(x     ,y     ,n//2) #2사분면 
                quad_tree(x+n//2,y     ,n//2) #1사분면 
                quad_tree(x     ,y+n//2,n//2) #3사분면                
                quad_tree(x+n//2,y+n//2,n//2) #4사분면 
                result += ')'
                double_break = True
                break
    if not double_break:
        if color == 1:  #검정색
            result += '1'
        else:           #흰색
            result += '0'

N = int(input())
data = [list(map(int,input().rstrip())) for _ in range(N)]

result = ''
quad_tree(0,0,N)

print(result)