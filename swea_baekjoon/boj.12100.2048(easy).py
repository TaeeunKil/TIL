from copy import deepcopy

N = int(input())

dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

ans = -1

def moving(r, c, d, board, merged):
    value = board[r][c]
    if value != 0:
        new_r = r + dr[d]
        new_c = c + dc[d]
        while 0<=new_r<N and 0<=new_c<N and board[new_r][new_c] == 0:
            new_r += dr[d]
            new_c += dc[d]
        if new_r == -1 or new_c == -1 or new_r == N or new_c == N:
            new_r -= dr[d]
            new_c -= dc[d]
        board[r][c] = 0
        if board[new_r][new_c] == 0:
            board[new_r][new_c] = value
        else:
            if board[new_r][new_c] == value and not merged[new_r][new_c]:
                board[new_r][new_c] = value*2
                merged[new_r][new_c] = 1
            else:
                board[new_r-dr[d]][new_c-dc[d]] = value


def dfs(matrix ,steps=0):
    global ans


    if steps == 5:
        biggest = 0
        for i in range(N):
            for j in range(N):
                biggest = max(biggest, matrix[i][j])
        ans = max(ans, biggest)
        return
    
    

    for d in range(len(dr)):
        board = deepcopy(matrix)
        if dr[d] == 1:
            merged = [[0]*N for _ in range(N)]
            for r in range(N-2, -1, -1):
                for c in range(N):
                    moving(r, c, d, board, merged)
            dfs(board, steps+1)

        elif dr[d] == -1:
            merged = [[0]*N for _ in range(N)]
            for r in range(1, N):
                for c in range(N):
                    moving(r, c, d, board, merged)
            dfs(board, steps+1)

        elif dc[d] == 1:
            merged = [[0]*N for _ in range(N)]
            for c in range(N-2,-1,-1):
                for r in range(N):
                    moving(r,c,d,board, merged)
            dfs(board, steps+1)
        
        elif dc[d] == -1:
            merged = [[0]*N for _ in range(N)]
            for c in range(1, N):
                for r in range(N):
                    moving(r,c,d,board, merged)
            dfs(board, steps+1)
    
    
matrix = [list(map(int, input().split())) for _ in range(N)]
dfs(matrix)
print(ans)