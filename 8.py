def g1(number):
    number = str(number)
    number = list(number)
    number.sort(reverse = True)
    number = ''.join(number)
    return int(number)

def g2(number):
    number = str(number)
    number = list(number)
    number.sort()
    number = ''.join(number)
    return int(number)

def f(number):
    number = g1(number)-g2(number)
    return number
    
N,K = map(int,input().split())
for i in range(K):
    N = f(N)
print(N)
