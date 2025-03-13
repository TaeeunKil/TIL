from collections import deque
from copy import deepcopy


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def bombing(coord, M):
    matrix = deepcopy(M)
    q = deque()
    visited = [[0]*H for _ in range(W)]
    q.append(coord)
    coord_i, coord_j = coord
    visited[coord_i][coord_j] = 1
    while q:
        cur_i, cur_j = q.popleft()
        block_no = matrix[cur_i][cur_j]
        if block_no == 1:
            visited[cur_i][cur_j] = 1
            continue
        else:
            for d in range(4):
                for n in range(1, block_no):
                    new_i = cur_i + di[d]*n
                    new_j = cur_j + dj[d]*n
                    if 0 <= new_i < W and 0 <= new_j < H:
                        if matrix[new_i][new_j] !=0 and not visited[new_i][new_j]:
                            q.append((new_i, new_j))
                            visited[new_i][new_j] = 1

    for a in range(W):
        for b in range(H):
            if visited[a][b] == 1:
                matrix[a][b] = 0   # 매트릭스 비우기

    for i in range(len(matrix)):
        new_list = [n for n in matrix[i] if n != 0]
        padding = [0] * (H - len(new_list))
        matrix[i] = padding + new_list  # 빈 칸을 왼쪽에, 블록을 오른쪽에
    return matrix


def top_list(matrix):
    top = [0] * W
    for i in range(W):
        w = matrix[i]
        for j, bomb in enumerate(w):
            if bomb != 0:
                top[i] = (i, j)
                break
        else:
            top[i] = 0
    return top


def dfs_max(matrix, c=0):
    global ans
    if c == N:
        remain = 0
        for a in range(W):
            for b in range(H):
                if matrix[a][b] != 0:
                    remain += 1
        if remain < ans:
            ans = remain
        return

    if matrix == [[0]*H for _ in range(W)]:
        ans = 0
        return
    top = top_list(matrix)
    for coord in top:
        if coord == 0:
            continue
        else:
            dfs_max(bombing(coord, matrix), c+1)


T = int(input())
for t in range(1, 1+T):
    N, W, H = map(int, input().split())
    input_matrix = [list(map(int, input().split())) for _ in range(H)]
    block_matrix = [[0]*H for _ in range(W)]

    for i in range(H):
        for j in range(W):
            block_matrix[W-j-1][i] = input_matrix[i][j]
    ans = float('inf')
    dfs_max(block_matrix)
    print(f'#{t} {ans}')

