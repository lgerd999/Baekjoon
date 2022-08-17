# https://www.acmicpc.net/problem/2798
# 완전탐색 + 백트래킹
import sys
input = sys.stdin.readline

'''
고려사항
1. 3장의 카드의 합이 M과 같거나 가깝거나 만들어야 함
2. 3장의 카드의 합을 출력
'''
def dfs(csum, index, path):
    global result
    global ssum
    # 목표값을 초과한 경우 탐색을 종료한다. 즉, csum - cards[i]값이 -값이면 이미 값을 초과한 것이다.
    if csum < 0:
        return
    # 카드 3장이 넘어가면 리턴한다.    
    if len(path) > 3:
        return
    # 카드 장수 중 중복되는 수가 있으면 리턴한다    
    if len(set(path)) != len(path):
        return
    # csum의 초기값은 target이며, csum의 0은 target과 일치하는 답이므로 result에 추가하고 탐색을 종료한다.                    
    if ssum > csum and len(set(path)) == 3: # 카드 3장이 모두 다른 수이고 카드 합이 M에 가까운 조합을 추가한다
        print('1=',csum,ssum)
        ssum = csum         # csum의 최소값이 M과 가장 가까운 수
        result.append(path)
        return
    
    for i in range(index, N):
        dfs(csum - cards[i], i, path + [cards[i]])
    
    '''

    '''
    print('else',result,ssum,csum)     
    #     # 메모리 초과 방지
    if result:
        result.pop()            
    return M-ssum

N,M = map(int,input().split())
cards = list(map(int,input().split()))
result = []
ssum = sys.maxsize

print(dfs(M,0,[]))