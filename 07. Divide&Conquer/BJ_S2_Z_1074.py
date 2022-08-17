# https://www.acmicpc.net/problem/1074

# def matrix_print(grid):
#     for i in range(len(grid)):
#         for j in grid[i]:
#             print(j,end=' ')
#         print()    

def DC(x,y,n):
    global cnt
    if x == R and y == C:
        print(cnt)
        exit()

    if n == 1:
        cnt += 1
        # paper[x][y] = cnt
        return
    # x+n 이 R 또는 C 보다 크지 않는다면, 해당 분면에 원하는 좌표가 없다고 판단하고 패스하고 다음 사분면으로 이동
    if not (x <= R < x + n and y <= C < y + n):
        cnt += n * n
        return
 
    k = n//2
    DC(x,y,k)    # 1사분면
    DC(x,y+k,k)  # 2사분면   
    DC(x+k,y,k)  # 3사분면
    DC(x+k,y+k,k)

cnt = 0
N,R,C = map(int,input().split())
N = pow(2,N)
# paper = [[0]*N for _ in range(N)]
DC(0,0,N)
# matrix_print(paper)
#print(paper[R][C])
