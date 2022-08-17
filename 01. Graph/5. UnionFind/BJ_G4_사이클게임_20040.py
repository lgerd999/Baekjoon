# https://www.acmicpc.net/problem/20040
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
def find_parent(x):
    if x == parent[x]: return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x,y):
    x,y = find_parent(x),find_parent(y)
    if x < y :
        parent[y] = x
    else:
        parent[x] = y

N,M = map(int,input().split())

# 부모 노드 리스트 초기화
parent = [i for i in range(N)]

for i in range(M):
    a,b = map(int,input().split())    
    # a와 b가 이미 연결되어 있는 상태로 같은 부모를 가지고 있는 상태에서 새로운 a와 b 입력에 대해 find 함수를 실행하면 싸이클이 발생함
    if find_parent(a) == find_parent(b):        
        print(i+1)
        sys.exit()
    else:    
        union_parent(a,b)
print(0)        
    