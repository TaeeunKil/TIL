from itertools import permutations
from itertools import product
from collections import deque
from copy import deepcopy


def rotate(arr, i):
    arr_t = deepcopy(arr)
    rotated_matrix[i].append(arr_t)
    for _ in range(3):
        arr_t = list(map(list, zip(*arr_t[::-1])))
        rotated_matrix[i].append(arr_t)

def bfs(cube):
    global ans
    q = deque()
    cnt = 0
    v = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    if cube[0][0][0] == 1 and cube[4][4][4] == 1:
        q.append((0, 0, 0, cnt))
        v[0][0][0] = 1

    while q:
        l = len(q)
        for _ in range(l):
            cz, cx, cy, c_cnt = q.popleft()
            if cx == 4 and cy == 4 and cz == 4:
                # ans = min(ans, c_cnt)
                if c_cnt < ans:
                    ans = c_cnt
                return
            for dz, dx, dy in directions:
                nz = cz + dz
                nx = cx + dx
                ny = cy + dy

                if 0<=nx<5 and 0<=ny<5 and 0<=nz<5:
                    if v[nz][nx][ny]==0 and cube[nz][nx][ny]==1:
                        q.append((nz, nx, ny, c_cnt+1))
                        v[nz][nx][ny] = 1


ans = float('inf')
directions = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,1), (0,0,-1)]            
    


matrix = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
rotated_matrix = [[] for _ in range(5)]


for i in range(5):
    rotate(matrix[i], i)

# pprint(rotated_matrix)
floor_idx = list(permutations(range(5)))
# 회전 인덱스 생성하기
rotated_idx = list(product(range(4), repeat=5))

# pprint(rotated_idx)

# 1 ~ 5층을 쌓기 위한 순열 조합 만들기 회전 중복순열에서 인덱스 받아오기
for per in permutations(range(5)):
    for idx_s in rotated_idx:
        cube = [0,0,0,0,0]
        for idx,(i, j) in enumerate(zip(per, idx_s)):
            cube[idx] = rotated_matrix[i][j]
        # pprint(cube)
        bfs(cube)

if ans == float('inf'):
    print(-1)
else:
    print(ans)