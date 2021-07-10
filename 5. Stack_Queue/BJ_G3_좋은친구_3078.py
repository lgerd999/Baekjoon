# https://www.acmicpc.net/problem/3078

N,K = map(int,input().split())
students = [0] * N
data = [0] * 21 # 2 ~ 20글자
count = 0
'''
Students[성적순] = 학생 이름 길이 저장 
Data[이름 길이] = Data에는 길이별 Count (최대 20글자까지)
Students[1등] = Cynthia(7) 
Students[2등] = Lloyd(5)   
Students[3등] = Stevie(6)  
Students[4등] = Kevin(5),   1~4등 사이 len = 5(2등, 4등) 
Students[5등] = Malcolm(7), 1등 제외,2~5등 사이 업데이트 사항 없음,                   
Students[6등] = Dabney(6),  2등 제외,3~6등 사이 3등과 동일한 길이 6를 가진 사람 = 6등
                            

Students[Name]         K----------->
Name length = 0  1  2  3  4  5  6  7
      Data = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] Cynthia, count = 0
             [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] Lloyd, count = 0
             [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] Stevie, count = 0
             [0, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] Kevin, count = 1
             [0, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] Malcolm, count = 1
             [0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] Dabney, count = 2

'''
for rank in range(N):   # rank = 성적, 1등부터
    name = len(input())
    students[rank] = name   # 학생 이름의 길이 저장
    if rank > K:            # 만약 학생의 등수가 K보다 커지는 경우
        data[students[rank - K - 1]] -= 1   # 자신과 상관 없는 등수의 학생을 제거
    count += data[name]     # 자신과 이름의 길이가 같은 친구를 쌍으로 추가
    data[name] += 1         # 이름의 길이를 저장하는 리스트에 자신을 추가
    print(students,data,count)

print(count)


