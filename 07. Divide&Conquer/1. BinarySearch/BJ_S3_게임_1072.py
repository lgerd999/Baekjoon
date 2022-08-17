# https://www.acmicpc.net/problem/1072
#
'''
게임 횟수 : X
이긴 게임 : Y
Z 는 승률(%). 소수점은 버린다. 게임을 몇 번 더해야 Z가 변하는지에 대한 프로그램.
예) X = 10, Y = 8
Z = 8/10 * 100 = 80
mid = (0+2)/2 = 1
--> 9/11 * 100 = 81, 
'''
import sys
input = sys.stdin.readline

X,Y = map(int,input().split())

def check(m):
    Z = (Y+m)*100//(X+m)    # int(Y/X)*100 으로 계산하면 틀렸다고 나옴. Y*100//X로 연산해야 함.
    return Z

start = 1
end = X
Z = check(0)
ans = -1
while start <= end:
    mid = (start+end)//2
    # Z보다 승률이 같거나 낮아지면 시작 위치 증가
    if check(mid) <= Z:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)            
