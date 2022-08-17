import sys 

def input_data(): 
    readl = sys.stdin.readline 
    N = int(readl()) 
    info = [list(map(int, readl().split())) for _ in range(N)] 
    return N, info 

    
    
sol = 0 

# 입력받는 부분 
#N, info = input_data() 
N = 3
info = [[3, 7], [15, 7], [5, 2]]

# 여기서부터 작성 
paper = [[0] * 101 for _ in range(101)]
visited = [[0] * 102 for _ in range(102)]

cnt = 0
for n in range(N):
    x = info[n][0]
    y = info[n][1]
    for i in range(x,x+10):
        for j in range(y,y+10):
            paper[i][j] = 1

for i in range(len(paper)):
    for j in range(len(paper[0])):
        if paper[i][j] == 1:
            cnt += 1

print(cnt)
