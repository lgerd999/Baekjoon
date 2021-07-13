# https://www.acmicpc.net/problem/1764
'''
* sys.stdin.readline을 사용시 input() 으로 입력받을 때 개행문자까지 같이 붙어옴
* 아래와 같이 입력을 받아야 하는 경우 sys.stdin.read().splitlines()를 사용한다.
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
단, 입력이 끝난 후 Ctrl + z를 눌러야 결과가 도출된다.
하지만, 답 제출시에는 Ctrl + Z를 누를 필요 없다.

'''
import sys

N,M = map(int,input().split())
names = sys.stdin.read().splitlines()

l_names = set(names[:N])
s_names = set(names[N:])
ans = list(l_names & s_names)
print(len(ans))
print(*sorted(ans),sep='\n')
