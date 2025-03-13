from collections import deque

T = int(input())

up = (-1,0)
down = (1,0)
left = (0, -1)
right = (0, 1)
directions = [up, down, left, right]

valid_direction ={
    1 : [up, down, left, right],
    2 : [up, down],
    3 : [left, right],
    4 : [up, right],
    5 : [down, right],
    6 : [left, down],
    7 : [up, left],
    up : [1, 2, 5, 6],
    down : [1, 2, 4, 7],
    left : [1, 3, 4, 5],
    right : [1, 3, 6, 7],
}


def dfs(R, C, hours):
    if hours > L:
        return
    
    visited[R][C] = hours
    
    cur_v = matrix[R][C]
    
    for dir in valid_direction[cur_v]:
        dr, dc = dir
        new_r, new_c = R + dr, C + dc
        if 0<= new_r <N and 0<= new_c <M:
            if visited[new_r][new_c] > hours+1:
                new_v = matrix[new_r][new_c]
                if new_v in valid_direction[dir]:
                    dfs(new_r, new_c, hours+1)
                        
                        
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    visited = [[float('inf')]*M for _ in range(N)]
    
    dfs(R,C,1)
    
    ans = 0
    for visit_row in visited:
        ans += M - visit_row.count(float('inf'))
    print(f'#{tc}', ans)
