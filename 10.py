N = int(input())
box = []
i = 1  
while i <= N**0.5:  
    if N % i == 0:
        box.append(i)
        if i != N//i:
            box.append(N//i)
    i += 1

box.sort()
for i in box:
    print(i)
