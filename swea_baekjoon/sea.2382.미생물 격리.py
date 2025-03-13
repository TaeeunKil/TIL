import sys
sys.stdin = open("input.txt", "r")

directions = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]
change_dir = [0, 2, 1, 4, 3]

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    matrix = [[0]*N for _ in range(N)]
    microes = []
    
    for _ in range(K):
        microes.append(list(map(int,input().split())))   
        
    for _ in range(M):
        for i in range(K):
            if microes[i] == 0:
                continue
            micro = microes[i]
            cur_r, cur_c, cur_v, cur_dir = micro
            dr, dc = directions[cur_dir]
            new_r = cur_r + dr
            new_c = cur_c + dc
            new_dir = cur_dir
            new_v = cur_v
            if new_r == 0 or new_r == N-1 or new_c == 0 or new_c == N-1:
                new_v //= 2
                if new_v == 0:
                    microes[i] = 0
                    continue
                new_dir = change_dir[cur_dir]
            microes[i] = [new_r, new_c, new_v, new_dir]
        
        
        r = 0
        c = 1
        v = 2
        dir = 3
        # microes의 인덱스 의미

        
        for j in range(K):
            if microes[j] == 0:
                 continue
            ar = microes[j][r]
            ac = microes[j][c]
            check = []               
            for k in range(K):
                if j == k or microes[k] == 0:
                    continue
                
                br = microes[k][r]
                bc = microes[k][c]
                if ar == br and ac == bc:
                    if check == []:
                        check.append((microes[j][v], microes[j][dir], j))
                    check.append((microes[k][v], microes[k][dir], k))
            
            sum_of_micro = 0
            max_value = -1
            max_index = -1
            for idx, same in enumerate(check):
                value, trash, remove_idx = same
                sum_of_micro += value
                if max_value < value:
                    max_value = value
                    max_index = idx
                if remove_idx == j:
                    continue
                microes[remove_idx] = 0
            if max_index != -1:
                microes[j] = [ar, ac, sum_of_micro, check[max_index][1]]
    
    ans = 0
    for micro in microes:
        if micro == 0:
            continue
        ans += micro[v]
    print(f'#{tc}', ans)
        
