from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

possible_coords = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            possible_coords.append((i, j))

n = len(possible_coords)

possible_wall = []

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            possible_wall.append((possible_coords[i], possible_coords[j], possible_coords[k]))

di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]

def virus_sepreads_bfs(matrix):
    q = deque()
    visited = [[0]*M for _ in range(N)]
    safe_zone = 0

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 2: # visited 확인 안 하는 이유는 다음에 visted 기반으로 돌려놓으려고
                q.append((i, j))
                while q:
                    cur_i, cur_j = q.popleft()
                    for dir in range(len(di)):
                        new_i = cur_i + di[dir]
                        new_j = cur_j + dj[dir]
                        if 0<= new_i <N and 0<= new_j <M:
                            if matrix[new_i][new_j] == 0 and not visited[new_i][new_j]:
                                matrix[new_i][new_j] = 2
                                visited[new_i][new_j] = 1
                                q.append((new_i, new_j))
    
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                safe_zone += 1
            elif matrix[i][j] == 2 and visited[i][j]:
                matrix[i][j] = 0
    
    return safe_zone


ans = 0
for wall in possible_wall:
    m = deepcopy(lab)
    for coord in wall:
        x, y = coord
        m[x][y] = 1
    safe = virus_sepreads_bfs(m)
    if ans < safe:
        ans = safe

print(ans)