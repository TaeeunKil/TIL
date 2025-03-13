T = int(input())

for tc in range(1, 1+T):
    N, K = map(int, input().split())
    crossword = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    ans = 0
    for row in crossword:
        count = 0
        for a in row:
            if a == 1:
                count += 1
            else:
                if count == K:
                    ans +=1
                count = 0
        if count == K:
            ans +=1
    for column in list(zip(*crossword)):
        count = 0
        for b in column:
            if b == 1:
                count += 1
            else:
                if count == K:
                    ans +=1
                count = 0
        if count == K:
            ans +=1
    print(ans)