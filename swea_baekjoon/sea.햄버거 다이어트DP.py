T = int(input())
for tc in range(1, T+1):
    N, L= map(int, input().split())
        
    dp = [0] * (L+1)
    for _ in range(N):
        taste, calories = map(int, input().split())
        for i in range(L, calories-1, -1):
            dp[i] = max(dp[i], dp[i-calories] + taste)
    print(f'#{tc}', dp[-1])
    
