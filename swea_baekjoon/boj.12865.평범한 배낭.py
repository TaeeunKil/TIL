N, K = map(int,input().split())
dp = [[0]*(K+1) for _ in range(N+1)]
W = [0]*(N+1)
V = [0]*(N+1)
for i in range(1,N+1):
    w, v = map(int,input().split())
    W[i], V[i] = w, v

for n in range(1, N+1):
    for w in range(1, K+1):
        dp[n][w] = dp[n-1][w]
        
        if W[n] <= w:
            dp[n][w] = max(dp[n][w], V[n]+ dp[n-1][w-W[n]])

print(dp[N][K])
