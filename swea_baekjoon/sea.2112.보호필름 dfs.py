from itertools import combinations
from copy import deepcopy

T = int(input())

def test_membrane(matrix):
    for check_list in zip(*matrix):
        if test_1 in ''.join(check_list) or test_0 in ''.join(check_list):
            continue
        return False
    return True


def state_to_tuple(matrix):
    # 각 행을 문자열로 합치거나 튜플로 변환해서 전체 상태를 튜플로 만듭니다.
    return tuple(''.join(row) for row in matrix)

def dfs(matrix, n=0, idx=0):
    global ans, visited
    
    state = state_to_tuple(matrix)
    if state in visited:
        return
    visited.add(state)
    
    if test_membrane(matrix):
        ans = min(ans, n)
        return
    
    if n >= ans or n >= K-1:
        return

    for i in range(idx, D):
        for all_a_or_b in inject:
            if matrix[i] == all_a_or_b:
                continue
            origin = matrix[i][:]
            matrix[i] = all_a_or_b
            dfs(matrix, n+1, i+1)
            matrix[i] = origin


for tc in range(1, T+1):
    
    D, W, K = map(int, input().split())
    test_1 = '1'*K
    test_0 = '0'*K
    inject = [list('0'*W), list('1'*W)]
     
    membranes = [list(input().split()) for _ in range(D)]
    ans = K
    visited = set()
    dfs(membranes)
    print(f'#{tc} {ans}')
