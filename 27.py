from collections import deque
n,m = map(int,input().split())
road = [[] for i in range(n+1)]

for i in range(m):
    A,B = map(int,input().split())
    road[A].append(B)

def count_sg(s):
    count = 1
    dqe = deque()
    visited = [False]*(n+1)
    
    visited[s] = True
    dqe.append(s)
    while 0 < len(dqe):
        now = dqe.popleft()
        for to in road[now]:
            if visited[to] == False:
                dqe.append(to)
                count+=1
                visited[to] = True
    return count
ans = 0

for i in range(1,n+1):
    ans += count_sg(i)

print(ans)