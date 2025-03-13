# import sys
# sys.stdin = open('input.txt', 'r')
from itertools import combinations

from pprint import pprint
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int,input().split())) for _ in range(N)]
    ans = float('inf')
    for comb in combinations(range(1,N), N//2 -1):
        selected = [0]+list(comb)
        unselected = list(set(range(N))- set(selected))
        a = 0
        b = 0
        for i in selected:
            for j in selected:
                if i == j:
                    continue
                a += S[i][j]
        for i in unselected:
            for j in unselected:
                if i == j:
                    continue
                b += S[i][j] 
        ans = min(ans, abs(a-b))       
        
    print(f'#{tc}', ans)