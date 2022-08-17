# https://www.acmicpc.net/problem/1966
# 제한 시간 2초. O(N^2)까지 가능

from collections import deque
result = []
T = int(input())
for i in range(T):
    N,M = map(int,input().split())  # N : 문서개수, M : 현재 큐에 몇 번째에 놓여있는지 나타내는 정수
    P = deque(list(map(int,input().split())))   # N개 문서의 중요도
    docu = deque([i for i in range(N)]) # 문서 A ~ A(N)
    cnt = 0
    while P:
        max_p = max(P)  # 중요도가 가장 높은 문서 구하기
        if max_p != P[0]:        # 중요도가 높은 문서가 큐 제일 앞에 있지 않는 경우
            idx = P.index(max_p)    # 중요도가 높은 문서의 index 구하기
            P.rotate(-idx)      # index만큼 Rotate해서 큐 제일 앞에 높이도록 함
            docu.rotate(-idx)   # 문서도 같이 Rotate해서 큐 제일 앞에 높이도록 해서 출력
        P.popleft()         # 큐 제일 앞 중요도 출력
        ans = docu.popleft()    # 큐 제일 앞으로 중요도 출력
        cnt += 1            # 출력 되었으면 몇 번째 출력되었는지를 나타내는 카운터 계산
        if ans == M:        # M 번째 출력이 완료되었다면, while 종료
            break        
    result.append(cnt)
print(*result,sep='\n')        