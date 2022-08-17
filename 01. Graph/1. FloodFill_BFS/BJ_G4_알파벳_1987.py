# https://www.acmicpc.net/problem/1987

'''
queue:{(0, 0, 'C')}
next:CD
next:CA
queue:{(1, 0, 'CD'), (0, 1, 'CA')}
next:CDK
next:CDE
queue:{(0, 1, 'CA'), (2, 0, 'CDK'), (1, 1, 'CDE')}
next:CAE
next:CAB...
'''

def bfs():
    rr = [-1,1,0,0]
    cc = [0,0,-1,1]
    # Q 중복 허용시 시간 초과 발생, 중복 경로는 집합으로 제거
    Q = set([(0,0,board[0][0])])
    cnt = 1
    while Q:
        r,c,alp = Q.pop()

        for n in range(4):
            nr = r + rr[n]
            nc = c + cc[n]

            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                continue

            if board[nr][nc] not in alp:                
                Q.add((nr,nc,alp + board[nr][nc]))
                cnt = max(len(alp)+1,cnt)           
    return cnt

N,M = map(int,input().split())    
board = [list(input().rstrip()) for _ in range(N)]

print(bfs())

'''
3 4
ABCD
BCDA
CDEF
ans : 6

10 10
ASWERHGCFH
QWERHDLKDG
ZKFOWOHKRK
SALTPWOKSS
BMDLKLKDKF
ALSKEMFLFQ
GMHMBPTIYU
DMNKJZKQLF
HKFKGLKEOL
OTOJKNKRMW
ans : 22

20 20
POIUYTREWQBWKALSLDLG
LKJHGFDSAMASFBMBOSOZ
NMBVCXZAKPAISJLBMROW
CEVTBFNIMLASNCVKNDKX
VPQLBKENMSAHBBLFOWPQ
ZLSKJJBNBEASZNFDGHHN
GPBMDLQDALAASBBXCEGA
APQIKBMROIBANPOBLMKS
ASKSKVJRPORHNOXZKSPN
LSNVOEOOOKAKANLGKOAX
AKVMBOTOWPQOJBSMSPEP
BLLBKWPEPBKNMROSALLP
BNQLDNBMKOVMEMELSLMA
RLEPQQPVKJRNBITNBSAS
ZXMCOITRPWKLPGKHNGMS
QOBKRPPPZSLEMPNKSPPR
OQJDNZNANDWKQKVJEOGJ
QUYVOIUYWERLKJHASDFV
ZCVWRETPOIUHJKLVBMAS
QWERZCVUIAFDKHSDFHSA
ans : 26

5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
ans : 10

'''