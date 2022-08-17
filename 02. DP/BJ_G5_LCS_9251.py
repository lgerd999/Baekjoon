# https://www.acmicpc.net/problem/9251
'''
str1 = ACAYKP
str2 = CAPCAK
      0  A  C  A  Y  K  P
0   [[0, 0, 0, 0, 0, 0, 0], 
C    [0, 0, 1, 1, 1, 1, 1], 
A    [0, 1, 1, 1, 2, 2, 2], 
P    [0, 1, 2, 2, 2, 3, 3], 
C    [0, 1, 2, 2, 2, 3, 3], 
A    [0, 1, 2, 2, 2, 3, 4], 
K    [0, 1, 2, 3, 3, 3, 4]]

점화식
str1[i] = str2[j], DP[i][j] = DP[i-1][j-1] + 1 : 왼쪽 대각선 위 방향에 1을 더한 값
str1[i]!= str2[j], DP[i][j] = max(DP[i-1][j],DP[i][j-1]) : 왼쪽 값과 위쪽 값 중 최대 값
'''
import sys
input = sys.stdin.readline
str1 = list(input().rstrip())
str2 = list(input().rstrip()) 
#print(str1,str2)

DP = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        if str1[i-1] == str2[j-1]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i][j-1],DP[i-1][j])
print(DP)            
print(DP[len(str1)][len(str2)])                
