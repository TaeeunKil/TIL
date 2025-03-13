from collections import deque


N, M= map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

vir_list = []
wall_list = []
directions = [(1,0), (0,1), (0,-1), (-1,0)]

for i in range(N):
    for j in range(N):
        value = lab[i][j]
        if value == 1:
            wall_list.append((i,j))
        elif value == 2:
            vir_list.append((i,j))

possible_vir = []

def dfs_vir(cnt = 0, idx=0):
    if cnt == M:
        min_list.append(virus_bfs(possible_vir))
        return
    
    for i in range(idx, len(vir_list)):
        possible_vir.append(vir_list[i])
        dfs_vir(cnt+1, i+1)
        possible_vir.pop()
        


def virus_bfs(virus_list):
    q = deque()
    new_lab = [[0]*N for _ in range(N)]
    for wall_i, wall_j in wall_list:
        new_lab[wall_i][wall_j] = 1
    for vir_i, vir_j in virus_list:
        new_lab[vir_i][vir_j] = 2
        q.append((vir_i,vir_j, 0))
    
    while q:
        l = len(q)
        for _ in range(l):
            cur_i, cur_j, time = q.popleft()
            ans = time
            for di, dj in directions:
                new_i, new_j = cur_i+di, cur_j+dj
                if 0<=new_i<N and 0<=new_j<N:
                    if new_lab[new_i][new_j] == 0:
                        new_lab[new_i][new_j] = time+1
                        q.append((new_i, new_j, time+1))
    if any(0 in row for row in new_lab):
            return N**2
    return ans

min_list = []
dfs_vir()

min_time = min(min_list)
if min_time == N**2:
    min_time = -1

print(min_time)
