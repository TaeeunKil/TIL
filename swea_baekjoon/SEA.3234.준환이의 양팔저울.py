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


# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     weights = list(map(int, input().split()))
#      
#     cache = {}
#  
#     def dfs(left_sum, right_sum, visited):
#         state = (left_sum, right_sum, visited)
#  
#         if state in cache:
#             return cache[state]
#  
#         if visited == (1 << N)-1:
#             return 1
#          
#         answer = 0
#         for i in range(N):
#             if not (visited & (1 << i)):
#                 w = weights[i]
#                 if left_sum >= right_sum + w:
#                     answer += dfs(left_sum, right_sum+w, visited|(1 << i))
#  
#                 answer += dfs(left_sum+w, right_sum, visited|(1 << i))
#          
#         cache[state] = answer
#         return answer
#  
#     answer = dfs(0, 0, 0)
#      
#     print(f'#{test_case} {answer}')