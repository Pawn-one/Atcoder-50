N = int(input())
S = list(input())
Q = int(input())

Box = [list(map(int,input().split())) for _ in range(Q)]

A = S[:len(S)//2]
B = S[len(S)//2:]

for t,a,b in Box:
    S = []
    if t == 1:
        S = A + B
        S[a-1],S[b-1] = S[b-1],S[a-1]
    else:
        S = B + A
        
    A = S[:len(S)//2]
    B = S[len(S)//2:]

print(''.join(S))