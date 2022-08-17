# https://www.acmicpc.net/problem/1654
#
import sys
input = sys.stdin.readline

K,N = map(int,input().split())
lan = [int(input()) for _ in range(K)]

'''
랜선 길이 4개가 있다고 하면, 이 랜선 길이가 같은 11조각이 필요한 상황. 그런데 랜선 길이는 최대가 되어야 한다.
---------------------
---------------
-------
----------
아이디어:
총 랜선 길이를 11로 나누면 평균이 나오는데 이것을 end 로 정의하고 이분 탐색을 시작.
mid 길이를 기준으로 각 랜선을 mid 로 나눈 총합이 11이 되는가를 체크해서 필요 랜선 갯수를 만족하지 않으면
end 길이를 mid -1로 줄이면서(즉, ) 다시 계산.
만약 필요 랜선 개수가 넘어가게 되면 mid+1이 start가 되면서 범위를 좁혀간다.

'''

start = 0
end = sum(lan)//N
# start 와 end가 같거나 역전되면 빠져나오기
while start <= end :
    total = 0
    mid = (start + end) //2    
    # K와 N이 모두 1인 경우 mid가 0이 되는 경우에 대한 예외 처리.
    if mid == 0:
        mid = 1
    for x in lan:
        total += x//mid
    # 필요한 랜선 갯수보다 작은 경우(왼쪽 부분 탐색)
    if total < N :
        end = mid -1
    # 필요한 랜선 갯수 보다 많은 경우(오른쪽 탐색)    
    else:
        # 최대한 덜 잘랐을 때가 정답이므로  result 변수에 기록
       result = mid
       start = mid + 1     

print(result)       
