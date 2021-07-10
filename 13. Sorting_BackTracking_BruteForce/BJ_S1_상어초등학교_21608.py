#https://www.acmicpc.net/problem/21608

from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())

# Define
seat = [[0]*N for _ in range(N)]    # 교실 배치도
rr = [-1,1,0,0]
cc = [0,0,-1,1]
ans = 0
student = defaultdict(list) # 학생 당 좋아하는 친구들을 저장하기 위해 딕셔너리로 정의
'''
NxN에 대해 완전 탐색 문제으로 각 자리에 대해 문제의 규칙에 따라 자리배치를 해야 하는 문제
N이 최대 20이기 때문에 최대 400개 자리에 대해서만 계산하면 되므로 브로드포스 방식으로 구현하면 됨
 - 20x20x20x20x4(640,000)
'''
for _ in range(N*N):
    fs = -1 # 비어 있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸을 계산하기 위한 변수
    es = -1 # 인접한 칸 중에서 비어있는 칸이 가장 많은 칸을 계산하기 위한 변수
    x,y =0,0    # 
    data = list(map(int,input().split()))
    student[data[0]].extend(data[1:])

    for i in range(N):
        for j in range(N):
            if seat[i][j] == 0: # 빈자리
                ecnt = 0
                fcnt = 0
                for n in range(4):  # set[i][j] 주변 상하좌우 체크
                    nr = i + rr[n]
                    nc = j + cc[n]
                    if nr < 0 or nc < 0 or nr >= N or nc >= N:
                        continue
                    if seat[nr][nc] in student[data[0]]:    # 좋아하는 학생들이 얼마나 있는지 카운트
                        fcnt += 1
                    if seat[nr][nc] == 0:   # 빈칸이 얼마나 있는지 카운트
                        ecnt += 1    
                # 상하좌우 중 좋아하는 학생이 가장 많은 칸에 대해 해당 좌표와 학생수를 기록
                # 좋아하는 학생수가 동일한 경우는 빈자리가 가장 많은 칸을 기록        
                if fs < fcnt or (fs == fcnt and es < ecnt):  
                    x,y = i,j
                    fs,es = fcnt,ecnt
    # 최종 자리 위치 x,y에 학생 자리 배치                
    seat[x][y] = data[0]
#만족도 조사    
for i in range(N):
    for j in range(N):
        cnt = 0
        for n in range(4):
            nr = i + rr[n]
            nc = j + cc[n]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue    
            if seat[nr][nc] in student[seat[i][j]]: # seat[i][j] 자리에서 좋아하는 학생이 있으면 카운트 +1 , 좋아하는 학생이 많이 분포되면 될수록 cnt 증가(만족도 상승) 
                cnt += 1
        if cnt !=0: # 완전 불만인 학생은 제외
            ans += pow(10,cnt-1)
print(ans)

