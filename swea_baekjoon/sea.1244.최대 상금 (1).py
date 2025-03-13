def dfs(num_str, swaps, dp):
    global ans
    if swaps == 0:
        ans = max(ans,int(num_str))
        return
    
    if (num_str, swaps) in dp:
        return 
    
    num_list = list(num_str)
    n = len(num_list)
    
    for i in range(n):
        for j in range(i + 1, n):
            num_list[i], num_list[j] = num_list[j], num_list[i]
            new_str = ''.join(num_list)
            dfs(new_str, swaps - 1, dp)
            # 백트래킹
            num_list[i], num_list[j] = num_list[j], num_list[i]
    
    dp[(num_str, swaps)] = 1

T = int(input())
for tc in range(1, T + 1):
    digits_str, K_str = input().split()
    K = int(K_str)
    dp = {}
    ans = 0
    dfs(digits_str, K, dp)
    print(f"#{tc} {ans}")