# https://www.acmicpc.net/problem/3111
#
'''
아래 문제는 아래 절차에 따라 구현되어야 한다. 
즉, 앞에서 A를 찾으면 삭제하고 종료하고, 뒤에서 앞의 방향으로 A를 찾아서 삭제하고 종료하는 반복 작업이다.

1.T에서 A를 찾아서 없으면 종료
2.T에서 A를 찾으면 A를 삭제
3.T에서 A를 찾아서 없으면 종료
4.T에서 마지막에 등장하는 A 를 찾아 삭제한다.
5. 1번으로 간다.

위 알고리즘에 따라, 앞과 뒤에서 인덱스를 저장할 변수가 필요하고 이를 저장할 공간이 필요함을 알 수 있다.

'''
import sys

input = sys.stdin.readline

A = list(input().rstrip())
T = input().rstrip()

front = []
back = []

r_A = A[::-1]  # 역방향에서 A 값
len_A = len(A)  # A의 길이

li = 0  # left index
ri = len(T)-1 # right index, 배열 길이를 고려했을 때 -1을 해 주어야 함.

# A를 찾아서 삭제하였다면, 지금이 front --> Back, 지금이 Back --> front 로 전환하기 위한 변수.
flag = False  # 초기값은 fron --> Back 을 나타내는 False로 설정.

while li <= ri:
    if not flag :
        front.append(T[li])
        li += 1  # fron에 문자하나씩 추가할때마 left index도 하나씩 증가. 이는 T에 대한 index이므로 front에서 A와 같을 시 index를 감소 고려안함.
        if front[-len_A:] == A:     # 문자열 끝에서 len_만큼 위치
            flag = True
            front[-len_A:] = []        
    else:
        back.append(T[ri])
        ri -= 1
        if back[-len_A:] == r_A:
            flag = False
            back[-len_A:] = []

# print(front,back)
# fron는 A의 앞까지 문자열이 저장, back은 뒷부터 역순으로 저장.
# back에 있는 문자열을 front에 붙이면서 다시 A와 같은 내용이 있는지 체크
while back:
    front.append(back.pop())  # back의 뒷 부터 front에 추가됨
    if front[-len_A:] == A:
        front[-len_A:] = []

# front의 변수는 리스트 타입이기 때문에 문자열로 변환
print(''.join(front))
            
            





'''
aba
ababacccababa

abcd
wrongabcabcabcdddanswer
--> 풀이과정
wrongabcabc abcd ddanswer
wrongabc abcd danswer
wrong abcd answer
wronganswer (답)

'''
