N,K = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
AB.sort()
num = 0
mo = K
for i in range(N):
    if i == 0:
        if K >= AB[i][0]:
            K += AB[i][1] - AB[i][0]
        else:
            print(K)
            exit()
    else:
        if K >= abs(AB[i-1][0]-AB[i][0]):
            K += AB[i][1] - abs(AB[i-1][0]-AB[i][0])
        else:
            print(AB[i-1][0] + K)
            exit()
print(K+AB[N-1][0])
