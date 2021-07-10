              
# https://www.acmicpc.net/problem/2531
# 참조 : https://blog.naver.com/sjy263942/222194700163
# 샘플 제품 사진 문제는 K가 가변적(모든 ID가 한번씩은 포함되어야 한다는 조건이 있어 window 사이즈가 가변적)이지만, 회전 초밥은 K가 고정적이라 해당 케이스만 찾으면되는 차이가 있음
# 윈도우 사이즈가 고정적인 경우, 윈도우 사이즈를 계산하는  함수를 사용하는 것은 시간 초과 우려가 있음

from collections import deque
               
# N = 8 # 회전 초밥 벨트에 놓인 접시의 수
# c = 30 # 쿠폰 번호
# K = 4 # 연속해서 먹는 접시의 수
# d = 30 # 가짓수
# D = [7,9,7,30,2,7,9,25] #벨트에 놓인 접시

N,d,K,c = map(int,input().split())
D = [int(input()) for _ in range(N)]
# print(D)

max_k = 0
window = deque(D[:K])

for i in range(N):
    #if len(set(window)) == K:   # K개 연속된 초밥의 길이(window)를 측정(집합 성질을 이용하여 중복된 값은 제거됨)
    ans = len(set(window))
    if c not in window:        # window 내 쿠폰 c가 없으면,
        ans += 1
    if max_k < ans:         # 연속된 초밥 배열 중에서 현재 값이 가장 크다면 업데이트
        max_k = ans       
    #print(window)
    window.popleft()                
    window.append(D[(i+K)%N])

print(max_k)

