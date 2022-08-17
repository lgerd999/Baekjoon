from heapq import heappush, heappop
from collections import defaultdict
from bisect import bisect_left,bisect_right

T = int(input())  # 테스트 케이스 개수. T는 1개 이상
result = []
for _ in range(T):
    R = defaultdict(int) # 운전자 이동 범위, 출발점은 key, 도착점은 value
    X = defaultdict(int) # 승객 번호는 key, 승객이 가고자 하는 거리는 value
    Q = []
    
    N, M = map(int, input().split())  # N은 승객수, M은 운전자수, N과 M은 1보다 크다
    for i in list(map(int, input().split())): # 모든 승객은 1 미터 이상은 간다.
        X[i] += 1                       # 승객 당 갈 수 있는 운전자 수 카운트
        # heappush(XQ,-i)
    
    for _ in range(M):        # 모든 운전자는 1미터 이상 1,000,000,000 미터 범위내에서 움직인다
        Y,Z = map(int, input().split())
        R[Y] = Z
        heappush(Q,-Y)  # 최대힙 정렬을 위해 -Y로 입력

    Xs = sorted(list(X.keys()))        
    cnt = 0
    for r in range(len(Q)):
        left = bisect_left(Xs,-Q[r])    
        # right = bisect_right(Xs,R[-YQ[r]])
        # print(-YQ[r],R[-YQ[r]],left,right)
        
        if left < len(Xs) and Xs[left] <= R[-Q[r]]:
            cnt += 1
            X[R[Xs[left]]] -= 1
            if X[R[Xs[left]]] == 0:
                del X[R[Xs[left]]]
                Xs.remove(Xs[left]) 
    print(cnt)

