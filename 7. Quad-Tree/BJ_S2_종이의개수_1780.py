# S2 https://www.acmicpc.net/problem/1780
#

def quad_tree(x,y,n):
    global Minus,Plus,Zero       # 파란색과 흰색 카운트 변수
    color = data[y][x]  # 기준 정의(-1,0,1)
    double_break = False

    for i in range(x, x+n):
        if double_break: break            
        for j in range(y, y+n):
            if data[j][i] != color:     # 기준 색생과 틀릴시에 재귀문 호출
                # 9사분면
                k = n//3
                quad_tree(x,       y      , k) 
                quad_tree(x,       y +   k, k)                 
                quad_tree(x,       y + 2*k, k)                                 
                
                quad_tree(x +   k, y      , k) 
                quad_tree(x +   k, y +   k, k) 
                quad_tree(x +   k, y + 2*k, k)                                                            
                
                quad_tree(x + 2*k, y      , k) 
                quad_tree(x + 2*k, y +   k, k) 
                quad_tree(x + 2*k, y + 2*k, k)                                                           
                
                double_break = True #탈출!
                break
    
    if not double_break:        
        if color == 1: # 1
            Plus += 1
        elif color == -1: # -1
            Minus += 1    
        else:
            Zero += 1 # 0



N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
Zero,Minus,Plus = 0,0,0

quad_tree(0,0,N)
print(Minus)
print(Zero)
print(Plus)


