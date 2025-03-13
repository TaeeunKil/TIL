T = int(input())
for tc in range(1,T+1):
    r, a, b = map(int, input().split())
    l = 1
    start = l
    end = r
    a_count= b_count= 0
    while start <= end:
        middle = (start + end)//2
        a_count += 1
        if middle == a:
            break
        elif middle > a:
            end = middle-1
        else:
            start = middle+1
    
    start = 1
    end = r

    while start <= end:
        middle = (start + end)//2
        b_count += 1
        if middle == b:
            break
        elif middle > a:
            end = middle-1
        else:
            start = middle+1
    
    print(f'#{tc}', end = ' ')
    if a_count == b_count:
        print(0)
    elif a_count > b_count:
        print('B')
    else:
        print('A')
    


