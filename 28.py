h,w,k = map(int,input().split())
box = [list(input()) for _ in range(h)]
count = 0

for row in range(1<<h):
    for column in range(1<<w):
        black_count = 0
        for bit_r in range(h):
            for bit_c in range(w):
                if row >> bit_r & 1 == 0 and column >> bit_c & 1 == 0:
                    if box[bit_r][bit_c] == '#':
                        black_count += 1
        if black_count == k:
            count += 1
print(count)