n,x = map(int,input().split())
x = x*100
for i in range(n):
    v,p = map(int,input().split())
    x -= v*p
    if x < 0:
        print(i+1)
        exit()
print(-1)