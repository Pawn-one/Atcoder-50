n = int(input())
box = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x1 = box[i][0]
            x2 = box[j][0]
            x3 = box[k][0]
            y1 = box[i][1]
            y2 = box[j][1]
            y3 = box[k][1]
            if (y3 - y1) * (x1 - x2) == (y1 - y2) * (x3 - x1):
                print('Yes')
                exit()
print('No')