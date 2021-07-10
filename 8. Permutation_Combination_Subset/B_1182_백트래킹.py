def combination(data):
    result = []
    def combin(index,path):
        result.append(path)
        for i in range(index,len(data)):
            combin(i+1,path+[data[i]])
    combin(0,[])        
    return result    

N, S = map(int,input().split())
data = list(map(int,input().split()))

# N, S = 5, 0
# data = [-7,-3,-2,5,8]

cnt = 0
for p in combination(data):
    print(p)
    if p ==[]:
        continue
    if sum(p) == S:
        cnt += 1

print(cnt)            