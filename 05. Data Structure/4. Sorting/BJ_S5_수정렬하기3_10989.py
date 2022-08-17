# 2751 문제 대비 시간제한은 3초 더 주고, 메모리 제한 258MB -> 8MB로 줄어 있음
# 시간보다는 메모리 소비 관점에서 접근 필요
# 입력값의 범위가 10000을 넘지 않으므로, 배열 10000개를 만들면 2byte * 10000 = 2MB 정도 예상됨. 초기값은 모두 0으로 셋팅.
# 입력 값을 해당 배열의 index로 하고 값은 +1씩 증가시킨다.
# 예를 들면, 5 2 3 1 4 2 3 5 1 7 이 입력값이면, array[5] += 1, array[2] += 1 이런식으로 하면, 
# arrary[0 1 2 3 4 5 6 7] = [0 2 2 2 1 2 0 1]
# 이제 count된 값의 수만큼만 print 해 주면 됨
# 파이선에서 입력/출력 성능 향상을 위해 입력에서는 sys.stdin.readlin을 사용하고, 출력에서는 sys.stdout.write(str(),+'\n')을 사용한다.

import sys
input = sys.stdin.readline
   
N = int(input())
# A = [int(input()) for _ in range(N)]
A = [0 for _ in range(100001)]

for i in range(N):    
    A[int(input())] += 1    

for i in range(10001):
    if A[i] != 0:
        for j in range(A[i]):
            sys.stdout.write(str(i)+'\n')    