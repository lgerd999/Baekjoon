# https://www.acmicpc.net/problem/7575

import sys
input=sys.stdin.readline

n,k=map(int,input().split())
data=[]
for _ in range(n):
    __=int(input())
    data.append(list(input().split()))

print(data)

for z in range(len(data[0])-k+1):   # 바이러스 코드 추정을 위한 최소 길이를 나타내는 정수 K
    t=data[0][z:z+k]    # 첫번째 프로그램 기준 index 0 ~ K 만큼 +1씩 window slicing 함
    print('t=',t)
    for m in range(1,n):    # 프로그램 개수
        can=''.join(data[m]).find(''.join(data[0][z:z+k]))  # 두번째 프로그램부터 시작하며, 기준 t 를 검색
        if can==-1: # 못찾으면
            print('sorry1',data[m],data[0][z:z+k])  
            can = ''.join(data[m][::-1]).find(''.join(data[0][z:z + k]))    # 뒤집어서 검색
        if can==-1: # 못찾으면
            print('sorry2',data[m][::-1],data[0][z:z+k])
            break
        print(can)
        if m==n-1:  # 찾으면
            print('YES')
            sys.exit()
print('NO')
