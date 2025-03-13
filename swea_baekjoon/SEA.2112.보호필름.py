from itertools import combinations
from copy import deepcopy

T = int(input())

def test_membrane(matrix):
    for check_list in zip(*matrix):
        if test_1 in ''.join(check_list) or test_0 in ''.join(check_list):
            continue
        return False
    return True
        
def injection(matrix):
    
    origin = deepcopy(matrix)

    if test_membrane(matrix):
        return 0

    for n in range(1, K+1):
        for chosen in combinations(range(D), n):
            for mask in range(1<<n):
                for i in range(n):
                    if mask & (1<<i):
                        matrix[chosen[i]] = inject_list[1]
                    else:
                        matrix[chosen[i]] = inject_list[0]

                if test_membrane(matrix):
                    return n
                
                for back in chosen:
                    matrix[back] = origin[back]
    return 'error'



for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    test_1 = '1'*K
    test_0 = '0'*K
    inject_list = [list('0'*W), list('1'*W)]
     
    membrane = [list(input().split()) for _ in range(D)]
    ans = injection(membrane)
    print(f'#{tc} {ans}')
