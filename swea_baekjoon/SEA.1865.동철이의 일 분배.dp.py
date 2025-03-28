# import sys
# sys.stdin = open('input (12).txt', 'r')

T = int(input())
def dfs(cnt, selected_mask):
    global ans
    
    if cnt == N:
        return 100
    
    # if selected_mask == (1<<N) -1:
    #   return 1    
    # 이것과 동일
    
    if memo[selected_mask] != -1:
        return memo[selected_mask]

    
    max_v = 0

    for i in range(N):
        if selected_mask & (1<<i):
            continue
        cur_prob = P[cnt][i] 
        if cur_prob == 0:
            continue
        candidate = cur_prob * dfs(cnt+1, selected_mask | (1<<i)) / 100
        max_v = max(max_v, candidate)

    memo[selected_mask] = max_v
    return max_v

for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    memo = [-1] * (1<<N)
    ans = dfs(0, 0)
    print(f'#{tc} {ans:7f}')

    
    
# dp로 할 수 있는 이유?
# 내 생각에는 갈수록 낮아질 수 밖에 없는 구조(계속 1보다 작은 값을 곱하므로)
# 따라서 곱의 최댓값을 갱신 계속하면 구할 수 있다?
# 혹은 메모를 해서 가지를 친다!

    
    
# P = [list(map(lambda x : x/100, map(int, input().split()))) for _ in range(N)]
# map의 각각 요소에 /100 적용시키기
# 람다로 적용가능하다!
# 
# 소수 몇째짜리 반올림은 round 지만
# 특정 소수 몇째짜리까지 반올림하고 전부 출력하라는 f'{ans:7f}' 로 표현 가능