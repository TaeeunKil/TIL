def combinations(idx=0, sum_of_heights =0):
    global ans, ans_is_B
    
    if sum_of_heights > B:
        ans = min(ans, sum_of_heights - B)
        return
    
    if sum_of_heights == B:
        ans = 0
        ans_is_B = True
        return
    
    if ans_is_B:
        return
    
    for i in range(idx, N):
        new_sum = sum_of_heights + H[i]
        combinations(i+1, new_sum)
    

T = int(input())

for tc in range(1, T+1):
    N, B = map(int,input().split())
    H = list(map(int, input().split()))
    ans = float('inf')
    ans_is_B = False
    combinations()
    print(f'#{tc} {ans}')