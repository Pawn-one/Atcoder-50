from collections import deque

s = input()
q = int(input())
t = [0] * q
f = []
c = []
s = deque(s)

for i in range(q):
    query = list(map(str,input().split()))
    if query[0] == '1':
        t[i] = int(query[0])
    elif query[0] == '2':
        t[i] = int(query[0])
        f.append(query[1])
        c.append(query[2])

T = 0
TT = 0

for i in range(len(t)):
    if t[i] == 1:
        T += 1
    elif t[i] == 2:
        if (int(f[TT]) + T) % 2 == 0:
            s.append(c[TT])
            # s = s + c[TT] 文字列の操作や配列の操作ではO(N)になる　
            # 文字列の型をdequeにすることで文字の追加などの計算量がO(1)になる
        else: 
            s.appendleft(c[TT])
            # s = c[TT] + s　文字列の操作や配列の操作ではO(N)になる
        TT += 1
s = ''.join(s)

if T % 2 == 0:
    print(s)
else:
    s = s[::-1]
    print(s)            

# sが文字列のとき　2226ms
# sがdequeのとき　215ms 
