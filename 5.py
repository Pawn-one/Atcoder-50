n,s,d = map(int,input().split())
mage = [list(map(int,input().split())) for _ in range(n)]
damage = 0
for i in range(n):
    if mage[i][0] < s and mage[i][1] > d:
        damage = 1
        break

if damage == 1:
    print('Yes')
else:
    print('No')