# https://www.acmicpc.net/problem/2630
# 참조 : https://claude-u.tistory.com/268

def quad_tree(x, y, n):
    global blue, white #주어진 배열과 색 카운트 끌어오기
    color = data[y][x] #첫 색깔과 나머지 색이 같아야함
    double_break = False #for문 탈출용 double_break
    
    for i in range(x, x+n):
        if double_break: break            
        for j in range(y, y+n):
            if data[j][i] != color: #하나라도 틀릴시에 재귀문 생성
                # rr = [n//2, 0,    0, n//2]
                # cc = [   0, 0, n//2, n//2]
                quad_tree(x, y, n//2) #2사분면
                quad_tree(x + n//2, y, n//2) #1사분면
                quad_tree(x, y + n//2, n//2) #3사분면
                quad_tree(x + n//2, y + n//2, n//2) #4사분면
                double_break = True #탈출!
                break
    
    if not double_break:
        if data[y][x] == 1: #파란색이라면
            blue += 1
        else:
            white += 1 #흰색이라면


N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
blue = 0
white = 0

print(data)

quad_tree(0,0,N)
print(white)
print(blue)


        
