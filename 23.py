N = int(input())
A = list(map(int,input().split()))
max_sum = -10**15

for i in range(N):
    min_num = A[i]
    for j in range(i,N):
        min_num = min(min_num,A[j])
        max_sum = max(max_sum,min_num*(j-i+1))

        #下記のコードは毎回min_numを配列の中から探すため遅い
        """min_num =  min(A[i:j+1])
           if min_num*(j-i+1) > max_sum:
                max_sum = min_num * (j-i+1)"""
        # 時間的には修正後コードは187ms
        # 修正前コードは1662ms と約10分の1になった
        
print(max_sum)