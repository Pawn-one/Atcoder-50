import itertools

N, K = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
route_box = []

for route in itertools.permutations(range(2, N + 1)):
    route_box.append((1,) + route + (1,))
count = [0] * len(route_box)

for i in range(len(route_box)):
    for j in range(N):
        count[i] += box[route_box[i][j]-1][route_box[i][j+1]-1]

print(count.count(K))

