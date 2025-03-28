import sys
sys.stdin = open('input (12).txt', 'r')

T = int(input())
def dfs(cnt, result):
    global ans
    
    if cnt == N:
        ans = max(ans, result*100)
        return
    
    if result*100 < ans:
        return
    
    if result == 0:
        return

    for i in selected.copy():
        new_result = result
        new_result *= P[cnt][i]
        selected.remove(i)
        dfs(cnt+1, new_result)
        selected.add(i)

for tc in range(1, T+1):
    N = int(input())
    P = [list(map(lambda x : x/100, map(int, input().split()))) for _ in range(N)]
    selected = set(range(N))
    ans = 0
    dfs(0, 1)
    print(f'#{tc} {ans:7f}')

    
# P = [list(map(lambda x : x/100, map(int, input().split()))) for _ in range(N)]
# map의 각각 요소에 /100 적용시키기
# 람다로 적용가능하다!
# 
# 소수 몇째짜리 반올림은 round 지만
# 특정 소수 몇째짜리까지 반올림하고 전부 출력하라는 f'{ans:7f}' 로 표현 가능