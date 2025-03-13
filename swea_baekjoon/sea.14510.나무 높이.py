T = int(input())
for tc in range(1,T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    max_h = max(trees)
    ans = -1
    number = [0, 0, 0]
    for tree in trees:
        needed = max_h - tree
        number[1] += needed%2
        number[2] += needed//2
    
    no_1 = number[1]
    no_2 = number[2]

    if no_1 <= no_2:
        while abs(no_1 - no_2) > 1:
            no_2 -= 1
            no_1 += 2
        if no_1 > no_2:
            remains = no_2*2 + 1
        elif no_1 <= no_2:
            remains = no_2*2

    elif no_1 > no_2:
        remains = no_1*2 -1

    ans = remains
    
    print(f'#{tc}', ans)