N = int(input())
count = 0
for i in range(1,int((2*N)**(1/2))):
    if 2*N % i == 0:
        x = i
        y = 2*N//i
        if x%2 != y%2:
            count += 2
print(count)