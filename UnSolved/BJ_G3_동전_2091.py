


data = [12, 5, 3, 1, 2]

tbl = [1,5,10,25]

coffee = data[0] #12원
coins = data[1:]


d = [0] * (coffee+1)

d[0] = 0

for i in range(3):
    for j in range(tbl[i],coffee+1):
        if d[j-tbl[i]] != 0:
            d[j] = max(d[j],d[j-tbl[i]] + 1)
            print(d)

print(d[coffee])            