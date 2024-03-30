n,m,x = map(int,input().split())

C = []
A = []
for i in range(n):
    CA = list(map(int,input().split()))
    C.append(CA[0])
    A.append(CA[1:])

#bit全探索
min_cost = 10**15
for i in range(1<<n):
    cost = 0
    skill = [0]*m
    for j in range(n):
        if (i >> j) & 1 == 1:
            cost += C[j]
            for k in range(m):
                skill[k] += A[j][k]
                
    if min(skill) >= x:
        min_cost = min(min_cost,cost)

if min_cost == 10**15:
    print(-1)
else:
    print(min_cost)

        