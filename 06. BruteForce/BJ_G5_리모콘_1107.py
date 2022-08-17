import sys
input = sys.stdin.readline
num = set(range(10))    # 0 ~ 9 버튼
current_ch = 100    # 현재 보고 있는 채널

N = int(input()) # 이동하려는 채널 번호
M = int(input())    # 리모컨에서 고장난 버튼 수
if M == 0:
    remokon = list(num) # 정상동작하는 버튼 리스트
else:        
    broken = set(map(int,input().split()))  # 고장난 버튼 입력
    remokon = list(num - broken)    # 정상동작하는 버튼 리스트

min_case = abs(current_ch - N)    # 현재 채널과 이동하려는 채널 사이의 차이 계산

for ch in range(1000000):    
    for j in range(len(str(ch))):
        if int(str(ch)[j]) not in remokon:
            break
        elif len(str(ch)) - 1 == j:
            min_case = min(min_case,abs(ch-N)+len(str(ch)))
            
print(min_case)           