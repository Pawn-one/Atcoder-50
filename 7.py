h,w,x,y = map(int,input().split())
box = [input() for _ in range(h)]

x -= 1
y -= 1
count = 1
#上
for i in range(1,h):
    if 0<=x-i<h:
        if box[x-i][y] == '#':
            break
        else:
            count += 1
#下
for i in range(1,h):
    if 0<=x+i<h:
        if box[x+i][y] == '#':
            break
        else:
            count += 1
#右
for i in range(1,w):
    if 0<=y+i<w:
        if box[x][y+i] == '#':
            break
        else:
            count += 1
#左
for i in range(1,w):
    if 0<=y-i<w:
        if box[x][y-i] == '#':
            break
        else:
            count += 1
print(count)