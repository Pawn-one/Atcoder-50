N = int(input())
h = list(map(int,input().split()))

cost = [10**15]*N
cost[0] = 0
for i in range(N-1):
    if cost[i+1] > abs(h[i+1] - h[i]) + cost[i]:
        cost[i+1] = abs(h[i+1] - h[i]) + cost[i]
    if i < N - 2 and cost[i+2] > abs(h[i+2] - h[i]) + cost[i]:
        cost[i+2] = abs(h[i+2] - h[i]) + cost[i]

print(cost[-1])   