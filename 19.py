x,k,d = map(int,input().split())
x = abs(x)

if 0 < x - k * d:
    print(abs(x - k * d))
else:
    count = k - abs(x // d)
    if count % 2 == 0:
        print(abs(x - d * (x//d)))
    else: 
        print(abs(x - d * ((x//d) + 1)))