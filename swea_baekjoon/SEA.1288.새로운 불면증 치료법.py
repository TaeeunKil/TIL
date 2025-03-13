T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    ans = set()
    i = 0

    while len(ans) < 10:
        i += 1
        N = n*i
        for a in map(int, list(str(N))):
            ans.add(a)
        
        
    print(f'#{tc} {n*(i)}')