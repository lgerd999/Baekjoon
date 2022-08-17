# https://www.acmicpc.net/problem/2352
# LIS
'''
n 개의 포트를 다른 n개의 포트와 연결해야 하는데 서로 꼬이지 않게 최대로 연결할 수 있는 개수를 구하는 프로그램

연결되는 포트가 서로 꼬이지 않고 최대로 연결되기 위해서는 오름 차순으로 정렬되어 있으면 된다.
문제에서 설명하는 그림을 보면, 다음과 같이 연결되어 있다.
<왼쪽 그림> 연결되어 있는 포트가 서로 꼬여 있다. 
1->4
2->2
3->6
4->3
5->1
6->5
여기서 꼬이지 않고 최대로 연결된 상태는 오른쪽 그림에 있다.(오름차순)
2->2
4->3
6->5
이는 최대 3개까지 꼬이지 않고 연결된다.
정리하자면,연결된 포트  4 2 6 3 1 5 에서 가장 긴 증가하는 부분 수열(LIS)을 찾으면 된다.

'''
import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
prog = list(map(int,input().split()))

# 이분 탐색을 이용한 방법
buf = [0]
for i in prog:
    if buf[-1] < i:
        buf.append(i)
    else:
        buf[bisect_left(buf,i)] = i
print(buf)
print(len(buf)-1)
