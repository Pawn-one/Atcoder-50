N,K = map(int,input().split())
p = list(map(int,input().split()))
p_exp = [0]*(N+1)
max_num = 0

for i in range(1,N+1):
    p_exp[i] = p_exp[i-1] + (p[i-1]+1)/2 

for i in range(K,N+1):
    if max_num < p_exp[i] - p_exp[i - K]:
        max_num = p_exp[i] - p_exp[i - K]

print(max_num)
    


    