import math

def dfs(cnt, left_sum, right_sum, visited):
    global ans
    
    state = (left_sum, right_sum, visited)
    
    if state in memo:
        return memo[state]

    if cnt == N:
        return 1
    
    # if visited == (1<<N) -1:
    #     return
    # (1<<N) -1 = 1*N, 전부 사용한 조건으로도 사용가능
    
    if max_sum - (left_sum + right_sum) < left_sum - right_sum:
        unselected = N-cnt
        return math.factorial(unselected) * (2**unselected) 
        
    
    result = 0
    
    for i in range(N):
        if visited & (1 <<i):
            continue
        result += dfs(cnt+1, left_sum+weights[i], right_sum, visited|(1<<i))
        
        if left_sum >= right_sum+weights[i]:
            result += dfs(cnt+1, left_sum, right_sum+weights[i], visited|(1<<i))
    
    memo[state] = result
    return result
    

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))
    weights.sort(reverse=True)
    max_sum = sum(weights)
    memo = {}
    ans = dfs(0,0,0,0)
    print(f'#{tc}', ans)