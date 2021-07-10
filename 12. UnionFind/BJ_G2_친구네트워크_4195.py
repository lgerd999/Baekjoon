#https://www.acmicpc.net/problem/4195
'''
Union Find 알고리즘
- 참조 : https://www.youtube.com/watch?v=Ha0w2dJa2Nk
- 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료 구조
- find 함수: 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
- union 함수 : 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산

'''
from collections import defaultdict
def find(x):
    # x와 parent가 같으면 x 노드를 return, 즉 x가 부모 노드
    if x == parent[x]: return x
    # 계속 중복을 피하기 위해 DP처럼 parent[x]에 계산된 값을 저장
    # 계속 부모 노트를 찾는 재귀함수
    else:
        p = find(parent[x])
        parent[x] = p
    return  parent[x]

def unite(x,y):  
    # 노드 x와 y의 부모 노드 찾기
    x,y = find(x),find(y)
    # x노드로 합친다.
    if x != y:  # xy 노드가 같은 부모 노드가 아닌 경우
        parent[y] = x   # 노드 x로 합친다
        num[x] += num[y]    # 친구 네트워크에 몇 명이 있는지 계산
'''
구현 아이디어
1. 부모 노드를 관리하기 위한 변수를 딕셔너리 타입으로 정의
 - 입력 변수가 문자열로 입력
2. 딕셔너리 key 값에 입력 데이터가가 없으면 부모 노드로 등록
3. 입력 데이터 합치기(union )
'''
ans = []
T = int(input())
for _ in range(T):    
    parent, num = defaultdict(int),defaultdict(int)
    F = int(input()) 
    for _ in range(F):
        a,b = input().split(" ")
        # parent key값에 없는 경우 부모 노드로 등록
        if a not in parent:
            parent[a] = a   #부모 노드로 설정
            num[a] = 1
        if b not in parent:
            parent[b] = b
            num[b] = 1
        unite(a,b)    # a와 b 노드는 친구 관계이므로 합친다
        ans.append(num[find(a)])
print(*ans,sep='\n')    
       
'''
1
8
a b
b c
d e
e f
g h
h i
a f
c i
'''