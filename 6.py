N = int(input())
mountain = [None]*N
for i in range(N):
    name,high = map(str,input().split())
    mountain[i] = [int(high),name]
mountain.sort(reverse=True)
print(mountain[1][1])