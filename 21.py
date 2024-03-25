a,b,w = map(int,input().split())
w_g = w*1000
min_ans = 10**15
max_ans = -10**15
for i in range(1,10**6+10):
    if a*i <= w_g <= b*i:
        min_ans = min(min_ans,i)
        max_ans = max(max_ans,i)
if min_ans == 10**15:
    print('UNSATISFIABLE')
else:
    print(min_ans,max_ans)