# https://www.acmicpc.net/problem/11664
# 삼분 탐색 : float 계산에 주로 사용.

from math import sqrt

data = list(map(int,input().split()))
A = data[0:3]
B = data[3:6]
C = data[6:9]

# print(A,B,C)

def distance(a,b):
    return sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2 + (b[2]-a[2])**2)

# print(distance(A,C))        
# print(distance(B,C))    

start = 0
end = 1.0
m = 0
while True:
    if abs(end-start) < 1e-9:
        m = (start+end)/2
        break
    m1 = start + (end-start)/3
    m2 = end - (end-start)/3
    
    m1x = A[0] + m1*(B[0]-A[0])
    m1y = A[1] + m1*(B[1]-A[1])
    m1z = A[2] + m1*(B[2]-A[2])
    m1A = list([m1x,m1y,m1z])
    
    m2x = A[0] + m2*(B[0]-A[0])
    m2y = A[1] + m2*(B[1]-A[1])
    m2z = A[2] + m2*(B[2]-A[2])
    m2A = list([m2x,m2y,m2z])
    
    d1 = distance(m1A,C)
    d2 = distance(m2A,C)
    
    if d1 > d2:
        start = m1
    else:
        end = m2    
X = list([ A[0] + m*(B[0]-A[0]), A[1] + m*(B[1]-A[1]), A[2] + m*(B[2]-A[2]) ])
print("%.10f"%distance(X,C))