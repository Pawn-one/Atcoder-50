N = int(input())
#「0と9を含む数列の個数」＝「数列全体の個数」ー「0または9を含まない数列の個数」と計算する
# 「0または9を含まない数列の個数」＝「0を含まない数列の個数」＋「9を含まない数列の個数」ー「0と9を含まない数列の個数」
#最後に全体を10^9+7で割る
#数列全体の個数
n = 10**9+7
nums_all = 10**N
nums_not0 = 9**N
nums_not9 = 9**N
nums_not09 = 8**N
num = nums_all - (nums_not0 + nums_not9 - nums_not09)
print(pow(num,1,n))
