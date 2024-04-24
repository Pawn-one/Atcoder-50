n,k = map(int,input().split())
r,s,p = map(int,input().split())
t = list(input())
score = 0
my_hands = [] 
for hand_num in range(n):
    if hand_num < k:
        if t[hand_num] == 'r':
            my_hands.append('p')
            score += p
        elif t[hand_num] == 's':
            my_hands.append('r')
            score += r
        else:
            my_hands.append('s')
            score += s
    
    else:
        if t[hand_num] == 'r':
            if my_hands[hand_num-k] == 'p':
                my_hands.append('x')
            else:
                score += p
                my_hands.append('p')
                
        elif t[hand_num] == 's':
            if my_hands[hand_num-k] == 'r':
                my_hands.append('x')
            else:
                score += r
                my_hands.append('r')
                
        elif t[hand_num] == 'p':
            if my_hands[hand_num-k] == 's':
                my_hands.append('x')
            else:
                score += s
                my_hands.append('s')        
print(score)
