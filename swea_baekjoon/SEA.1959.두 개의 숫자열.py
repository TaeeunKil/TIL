T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    if N <= M:
        for i in range(M-N+1):
            filtered = 0
            for j in range(N):
                filtered += A[j] * B[i+j]
                print(filtered)
            if ans < filtered:
                ans = filtered
    else:
        for i in range(N-M+1):
            filtered = 0
            for j in range(M):
                filtered += A[j+i]*B[j]
            if ans < filtered:
                ans = filtered

    print(f'#{tc} {ans}')