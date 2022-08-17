# https://www.acmicpc.net/problem/2143
# 
'''
부 배열의 합 = prefix_sum

A의 누적합과 B의 누적합을 구한다.
A의 누적합이 T를 넘어가면 안되고, B의 누적합이 T-A를 넘어가면 안된다.
prefix_A[i] , i = 0,...

'''
import sys
from bisect import bisect_left,bisect_right
input = sys.stdin.readline
 
T = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))

# C 리스트의 모든 조합의 합(keys)과 빈도(values)를 구하는 함수
def calc(C,num):
    result = dict()
    for i in range(num):
        hap = 0
        for j in range(i, num):
            hap += C[j]
            # get 메소드 : 딕셔너리 result의 key값 hap의 value를 반환하는데, 없는 key를 입력하는 경우 에러대신 None을 반환. 
            if result.get(hap,0):   # get(variable,0) 여기서 0은  None 대신 사용할 수 있는 값을 설정.
                result[hap] += 1
            else:
                result[hap] = 1
        print(result)                
    return result

ans = 0
X = calc(A,n)
Y = calc(B,m)
for i in X.keys():
    if Y.get(T-i):
        ans += (X[i]*Y[T-i])
        print(i,X[i],Y[T-i])
'''
X[i] = A[1]+ ...+A[i-1] + A[i]
Y[i] = B[1]+ ...+B[i-1] + B[i]

X[1](합이 1) + Y[5-1](합이 4) ==> A[1] + B[1] + B[2], A[3] + B[1] + B[2]
X[2](합이 2) + Y[5-2](합이 3) ==> A[4] + B[2]
X[3](합이 3) + Y[5-3](합이 2) ==> A[2] + B[3], A[3] + A[4] + B[3]
X[4](합이 4) + Y[5-4](합이 1) ==> A[2] + A[3] + B[1], A[1] + A[2] + B[1]

'''
print(ans)


##### 누적합과 이분 탐색으로 해결 #####
'''
def prefix_sum(C,num):    
    result = []
    for i in range(num):
        hap = 0
        for j in range(i,num):
            hap += C[j]
            result.append(hap)
    return result

ans = 0
X = prefix_sum(B,m)
X = sorted(X)
for i in prefix_sum(A,n):
    temp = T - i
    left = bisect_left(X,temp)
    right = bisect_right(X,temp)
    ans += right - left

print(ans)    
'''
##########################################
