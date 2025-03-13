T = int(input())
M = 13
for tc in range(1, T+1):
    day, month, three_month, year = map(int, input().split())
    swim_days = [0] + list(map(int, input().split()))
    dp = [0] * M
    for i in range(1, M):
        day_or_month= min(day * swim_days[i], month)
        if i > 3:
            dp[i] = min(dp[i-1] + day_or_month, dp[i-3] + three_month)
        else:
            dp[i] = min(dp[i-1] + day_or_month, three_month)
    ans = min(dp[-1], year)
    print(f'#{tc}', ans)