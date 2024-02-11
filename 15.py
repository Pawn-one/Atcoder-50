N = list(input())
number = sum(int(num) for num in N)

if number % 3 == 0:
    print(0)
    exit()
elif len(N) - (N.count('0')) == 1:
    print(-1)
    exit()

a_number = number % 3
a = []

for num in N:
    if int(num) % 3 != 0:
        a.append(int(num) % 3)

count1 = a.count(1)
count2 = a.count(2)

if a_number == 1:
    if count1 >= 1 and len(N) > 1:
        print(1)
    elif count2 >= 2 and len(N) > 2:
        print(2)
    else:
        print(-1)
        
elif a_number == 2:
    if count2 >= 1 and len(N) > 1:
        print(1)
    elif count1 >= 2 and len(N) > 2:
        print(2)
    else:
        print(-1)
