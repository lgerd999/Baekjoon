# https://www.acmicpc.net/problem/1107

from bisect import bisect_left,bisect_right
import sys
input = sys.stdin.readline

'''
고려사항
1. 고장난 버튼이 없는 경우가 있을 수 있다(M = 0). 그리고, 0인 경우 세번째 줄의 입력이 없다.
2. 현재 보고 있는 채널은 100번이므로 입력되는 채널과 비교해서 최소 버튼을 누르는 것을 선택해야 한다(min(100,N))
3. 채널 0에서 -버튼을 누른 경우 채널이 변하지 않는다.

'''
num = set(range(10))    # 0 ~ 9 버튼
current_ch = 100    # 현재 보고 있는 채널

N = input()
M = int(input())
if M == 0:
    remokon = list(num)
else:        
    broken = set(map(int,input().split()))  # 고장난 버튼 입력
    remokon = list(num - broken)    # 정상동작하는 버튼
remokon.sort()
cnt = 0
diff_check = sys.maxsize
min_S = '0'
min_cnt = 0
S = '0' # typeError 방지
for i in range(len(N)-1):       # 입력 채널의 자리수
    if int(N[i]) in remokon:    # 자리수 각각이 정상동작되는 버튼이라면,
        S += N[i]
        cnt += 1                # 누른 버튼 카운트
    else:                       # 고장난 버튼인 경우        
        # 첫번째 입력 채널 번호가 고장난 버튼 번호라면, 두번째 입력 채널번호까지 고려해서 누를 수 있는 가장 큰 번호를 누른다.
        # 단, 두 번째 입력 채널번호가 있다는 가정.                
        index = bisect_left(remokon,int(N[i:i+2]))          
        
        print(index,int(N[i:i+2]),sep=',') 
        if 0 < index < len(remokon):   # indexError 방지 , 0 <= index <= len(remokon)  
            # 인덱스가 정상동작 버튼의 숫자 중 왼쪽과 오른쪽 중 어느쪽에 차이가 적은쪽으로 인덱스 계산
            if abs(int(N[i])-remokon[index-1]) <= abs(int(N[i])-remokon[index]):
                index = index - 1                    
        elif index == len(remokon):
            index = index - 1 
        
        if diff_check > abs(int(N) - int(S)):
            min_cnt = abs(int(N) - int(S))
            min_S = S
            min_cnt = cnt

        if index >= 0:
            S += str(remokon[index])
            cnt += 1       # 누른 버튼 카운트

print('before=',N,S,cnt)
print('min=',min_S,min_cnt)
if abs(int(N) - int(S)) >= abs(int(N) - int(min_S)):
    S = min_S
    cnt = min_cnt
'''
실제 채널과 고장난 버튼을 고려한 입력 채널과의 차이를 계산해서 +,- 버튼을 누르는 횟수 계산 
 - 고장난 버튼을 고려하여 5457의 경우 4번 버튼을 누르고 난 최적의 값은 5459이며, -버튼을 2번 누르면 목표 채널에 도달
 - 고장난 버튼을 고려하여 100의 경우 3번 버튼을 누르고 난 최적의 값은 555이며, -버튼을 400번 눌러야 목표 채널 도달.
    그러나, 현재 보고 있는 채널이 100에서 목표 채널까지 +/-버튼을 눌러 도달할 수 있는 횟수 0이므로 최종 최솟값은 0
--> min(N - S가 +/- 버튼 횟수 + 숫자 입력 횟수, 100 에서 +/- 버튼 횟수)    

'''
# 100 일 때 0일 때에 대한 고려 필요        
if abs(int(N) - int(S))+cnt < abs(int(N) - 100):    # 자리수 입력 + N-S 만큼 +/- 로 이동하는 경우가 더 최소인 경우
    cnt += abs(int(N) - int(S))
elif abs(int(N) - int(S))+cnt >= abs(int(N) - 100): # 100 에서 +/-로 이동하는 것이 더 최소인 경우
    cnt = abs(int(N) - 100)
 
# diff = min(abs(N - int(S)),abs(N - 100))         
# cnt += diff
print('after=',N,S,cnt)        
print(cnt)        

'''
1555
8
0 1 3 4 5 6 7 9
ans = 670
--> 1555에서 888(+3)누르고 +버튼을 667번 누르면 총 670번임(OK)
--> 2222(+4)누르고 -버튼을 667번 누르면 총 671번임

444445
9
0 1 2 3 5 6 7 8 9
--> 444444(+6)에서 +버튼 1번 누르면 총 7번임(OK)

500000
2
1 5
--> 499999(+6) 누른 다음 +버튼 1번 눌러 총 7번임

11
8
1 3 4 5 6 7 8 9 
--> 2(+1) 누르고 +버튼 9번 눌러 총 10번임(OK)

12
9
0 1 3 4 5 6 7 8 9
--> 2(+1) 누르고 +버튼 10번 눌러 총 11번임

9999
1
9
--> 10000(+5) 누르고 -버튼 1번 눌러 총 6번임

0
9
0 1 2 3 4 5 6 7 9
--> 8(+1) 누르고 -버튼 8번 눌러 총 9번임

10
9
1 2 3 4 5 6 7 8 9
--> 11

1
10
0 1 2 3 4 5 6 7 8 9  
--> 99

2229
6
4 5 6 7 8 9
--> 5

10
1
0
--> 2

0
10
0 1 2 3 4 5 6 7 8 9
--> 100

9
8
0 3 4 5 6 7 8 9
--> 4

0
3
0 1 2
--> 4

''' 
    