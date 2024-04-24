N = int(input())
numbers = set()
if N == 1:
    print(1)
    exit()
    
for a in range(2,N):
    for b in range(2,N):
        if a**b > N:
            if b == 2:
                print(N - len(numbers))
                exit()
            break
        else:
            numbers.add(a**b)
        
