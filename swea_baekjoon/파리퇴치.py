

T =int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            flies = 0
            for k in range(M):
                for l in range(M):
                    flies += matrix[i+k][j+l]
            if ans < flies:
                ans = flies
    
    print(f'#{tc} {ans}')