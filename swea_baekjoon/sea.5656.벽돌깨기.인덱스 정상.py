from collections import deque
from copy import deepcopy
from pprint import pprint

directions = [(0,1), (1,0), (0, -1), (-1,0)]

def bombing(coord, M):
    matrix = deepcopy(M)
    q = deque()
    visited = [[0]*W for _ in range(H)]
    q.append(coord)
    coord_i, coord_j = coord
    visited[coord_i][coord_j] = 1
    while q:
        cur_i, cur_j = q.popleft()
        block_no = matrix[cur_i][cur_j]
        if block_no == 1:
            visited[cur_i][cur_j] = 1
            continue
        for dir in directions:
            di, dj = dir
            for n in range(1, block_no):
                new_i = cur_i + di*n
                new_j = cur_j + dj*n
                if 0 <= new_i < H and 0 <= new_j < W:
                    if matrix[new_i][new_j] !=0 and not visited[new_i][new_j]:
                        q.append((new_i, new_j))
                        visited[new_i][new_j] = 1
    # pprint(visited)
    for a in range(W):
        for b in range(H):
            if visited[b][a] == 1:
                matrix[b][a] = 0   # 매트릭스 비우기
                # print('------------------')
                # pprint(matrix)
                
                for c in range(b-1, -1, -1):
                    boom = matrix[c][a]
                    if boom != 0:
                        matrix[c+1][a] = boom
                        matrix[c][a] = 0
                
                # pprint(matrix)
                # print('--------------------')

    return matrix


def top_list(matrix):
    pprint(matrix)
    top = [0]*W
    for j in range(W):
        for i in range(H):
            if matrix[i][j] != 0:
                top[j] = (i, j)
                break
    return top


def dfs(matrix, c=0):
    global ans
    if c == N:
        remain = 0
        for a in range(H):
            for b in range(W):
                if matrix[a][b] != 0:
                    remain += 1
        ans = min(ans, remain)
        return

    if matrix == zero_matrix:
        ans = 0
        return
    
    top = top_list(matrix)
    print(top)
    for coord in top:
        if coord == 0:
            continue
        else:
            dfs(bombing(coord, matrix), c+1)


T = int(input())
for t in range(1, 1+T):
    N, W, H = map(int, input().split())
    input_matrix = [list(map(int, input().split())) for _ in range(H)]
    zero_matrix = [[0]*W for _ in range(H)]
    ans = float('inf')
    dfs(input_matrix)
    print(f'#{t} {ans}')

