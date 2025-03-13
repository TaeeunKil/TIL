from collections import deque
from copy import deepcopy
from itertools import combinations

N, M = map(int, input().split())

chiken = [list(map(int, input().split())) for _ in range(N)]

dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]


possible_chiken = []
for i in range(N):
    for j in range(N):
        if chiken[i][j] == 2:
            possible_chiken.append((i, j, 0))

ans = float('inf')


def chiken_distance_bfs(coord_list):
    global ans
    q = deque()
    matrix = deepcopy(chiken)
    result = 0
    
    for coord in coord_list:
        r, c, d = coord
        matrix[r][c] = 3 # 선택한 치킨집 3
        q.append(coord)
    while q:
        
        same_depth = len(q)
        for _ in range(same_depth):
            cur_r, cur_c, dist = q.popleft()
            for dir in range(len(dr)):
                new_r = cur_r + dr[dir]
                new_c = cur_c + dc[dir]
                if 0<=new_r<N and 0<=new_c<N:
                    if matrix[new_r][new_c] == 3:
                        continue

                    if matrix[new_r][new_c] == 1:
                        result += dist+1
                    matrix[new_r][new_c] = 3
                    q.append((new_r, new_c, dist+1))
    if ans > result:
        ans = result



for chiken_coord in combinations(possible_chiken, M):
    chiken_distance_bfs(chiken_coord)

print(ans)
