T = 10
for tc in range(1, T+1):
    N = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(N)]

    for c in range(N):
        for r in range(N):
            cur_val = magnetic[r][c]
            if cur_val == 2:
                magnetic[r][c] = 0
                new_r = r-1
                while new_r >= 0 and magnetic[new_r][c] == 0:
                    new_r = new_r - 1       
                if new_r == -1:
                    continue
                else:
                    magnetic[new_r+1][c] = cur_val
    ans = 0

    for c in range(N):
        for r in range(N):
            cur_val = magnetic[r][c]
            if cur_val == 2 and magnetic[r-1][c] == 1:
                ans += 1

    print(f'#{tc} {ans}')