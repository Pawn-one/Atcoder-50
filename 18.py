N = int(input())
nums = list(map(int,input().split()))
ans = 0
times = sum(nums)
mod = 10**9 + 7
for i in range(N):
    times -= nums[i]
    ans += nums[i]*times

print(ans%mod)

