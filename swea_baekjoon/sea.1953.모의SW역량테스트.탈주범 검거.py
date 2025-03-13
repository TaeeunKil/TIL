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


def bfs(R, C):
    q = deque()
    visited = [[0]*M for _ in range(N)]
    q.append((R, C, 1))
    visited[R][C] = 1
    ans = 0
    while q:
        cur_r, cur_c, cnt = q.popleft()
        if cnt > L:
            return ans
        cur_v = matrix[cur_r][cur_c]
        ans += 1
        for dir in valid_direction[cur_v]:
            dr, dc = dir
            new_r, new_c = cur_r + dr, cur_c + dc
            if 0<= new_r <N and 0<= new_c <M and not visited[new_r][new_c]:
                    new_v = matrix[new_r][new_c]
                    if new_v in valid_direction[dir]:
                        q.append((new_r, new_c, cnt+1))
                        visited[new_r][new_c] = 1
    return ans
                        
                        
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{tc}', bfs(R, C))





## 강사님 풀이 보니까
## 그냥 갈 수 있는 방향일 떄를 따로 관리하자