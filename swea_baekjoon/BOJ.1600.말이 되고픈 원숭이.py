from collections import deque

K = int(input())
W, H = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(H)]


knight_move = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
move = [(1,0), (0,-1), (-1,0), (0, 1)]


def monkey_bfs(i=0, j=0):
    q = deque()
    moves = 0
    knight_moves = 0
    q.append((i, j, moves, knight_moves))
    visited = [[[False]*W for _ in range(H)] for _ in range(K+1)]
    visited[knight_moves][i][j] = True
    while q:
        for _ in range(len(q)):
            cur_i, cur_j, cur_moves, cur_knight_moves = q.popleft()

            if cur_i == H-1 and cur_j == W-1:
                return cur_moves

            
            for di, dj in move:
                new_i = cur_i + di
                new_j = cur_j + dj
                if 0<= new_i < H and 0<= new_j < W:
                    if matrix[new_i][new_j] == 0 and not visited[cur_knight_moves][new_i][new_j]:
                        q.append((new_i, new_j, cur_moves+1, cur_knight_moves))
                        visited[cur_knight_moves][new_i][new_j] = True
        
            if cur_knight_moves < K:
                for di, dj in knight_move:
                    new_i = cur_i + di
                    new_j = cur_j + dj
                    if 0<= new_i < H and 0<= new_j < W:
                        if matrix[new_i][new_j] == 0 and not visited[cur_knight_moves+1][new_i][new_j]:
                            q.append((new_i, new_j, cur_moves+1, cur_knight_moves+1))
                            visited[cur_knight_moves+1][new_i][new_j] = True
    return -1

ans = monkey_bfs()
print(ans)