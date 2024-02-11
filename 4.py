n,x = map(int,input().split())
ans = []
A = list(map(int,input().split()))
for i in range(n):
    if A[i] != x:
        ans.append(A[i])
    
print(*ans)
    