# https://www.acmicpc.net/problem/10845
#
'''
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

'''
import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
Q = deque()

for _ in range(N):
    cmd = list(input().split())
    # print(cmd,Q)
    if cmd[0] == 'push':
        Q.append(cmd[1])
    elif cmd[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)    
    elif cmd[0] == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)    
    elif cmd[0] == 'size':
        print(len(Q))
    elif cmd[0] == 'empty':
        if Q:
            print('0')   
        else:
            print('1')    
    elif cmd[0] == 'pop':
        if Q:
            print(Q.popleft())
        else:
            print('-1')           