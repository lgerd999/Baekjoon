# https://www.acmicpc.net/problem/10775

# N = int(input())  # Gate 수
# P = int(input())  # 비행기 수
# data = [int(input()) for _ in range(P)]
#print(data)
N,P = 4,6
data = [2,3,3,4,4] #3

'''
# 정답 - pass 100%
def find(x):
    if x == parent[x]: # 해당 비행기가 도킹할 게이트가 비어 있으면 
        return x
    else:  # 해당 비행기(x)가 도킹할 게이트가 이미 차 있으면
        parent[x] = find(parent[x])  # unite 된 부모 게이트  
        return parent[x]

def unite(x,y):  # 도킹이 완료되면 또는 이미 완료되어 있으면 상위 게이트로 찾아서 교체
    x,y = find(x),find(y)
    parent[x] = y

parent = list(range(N+1))
count = 0
for plane in data:
    v=find(plane) # 도킹할 게이트 찾기
    if v != 0:  # 도킹할 게이트가 있으면
        unite(v,v-1)
        count += 1
    else:
        break
print(count)
'''

def find(x):
    if x == parent[x]: # 해당 비행기가 도킹할 게이트가 비어 있으면 
        return x
    else:  # 해당 비행기(x)가 도킹할 게이트가 이미 차 있으면
        parent[x] = find(parent[x])  # unite 된 부모 게이트  
        return parent[x]

docking = [0]*(N+1)
parent = list(range(N+1))
count = 0
for plane in data: # Gate    
    # 도킹이 안되어 있으면 바로 도킹하고, 부모 게이트는 상위(이전) 게이트로 설정
    if parent[plane] and docking[plane] == 0:
        parent[plane] = parent[plane-1]
        docking[plane] = 1
        count += 1
    else:
        '''
        #시간초과
        cnt = 1
        #도킹이 이미 되어 있으면 상위(이전) 게이트 찾기
        while docking[plane-cnt] == 1 and (plane- cnt) > 0:            
           cnt += 1         

        #부모게이트가 0이 아니고, 도킹이 아직 되어 있지 않은 게이트 찾기
        if parent[plane-cnt] and docking[plane-cnt] == 0:
           parent[plane-cnt] = parent[plane-cnt-1]
           docking[plane-cnt] = 1
           count += 1
        '''
        v = find(plane)        
        # 부모게이트가 0이 아니고, 도킹이 아직 되어 있지 않은 게이트 찾기
        if parent[v] and docking[v] == 0:
            parent[v] = parent[v-1]
            docking[v] = 1
            count += 1        
        else :
            break
    # print(parent)    
    # print(docking)                 
print(count)
