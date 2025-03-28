from collections import deque
from pprint import pprint

N = int(input())
islands = [list(map(int,input().split())) for _ in range(N)]

directions = [(1,0), (-1,0), (0,1), (0,-1)]

islands_borders = []

def make_border_set(r,c,i):
    q = deque()
    q.append((r,c))
    visited[r][c] = True
    
    while q:
        cur_r, cur_c = q.popleft()
        islands[cur_r][cur_c] = i
        for dr, dc in directions:
            new_r, new_c = cur_r + dr, cur_c + dc
            if 0<= new_r<N and 0<= new_c <N:
                if visited[new_r][new_c]:
                    continue
                if islands[new_r][new_c] == 0:
                    if (cur_r, cur_c) not in border_set:
                        border_set.add((cur_r, cur_c))
                    continue
                q.append((new_r, new_c))
                visited[new_r][new_c] = True
    
def min_bridge_length(r,c, i):
    q = deque()
    visited = [[False]*N for _ in range(N)]
    step = 0
    q.append((r,c,step))
    visited[r][c] = True
    
    while q:
        cur_r, cur_c, cur_steps = q.popleft()
        for dr, dc in directions:
            new_r, new_c = cur_r + dr, cur_c + dc
            if 0<= new_r<N and 0<= new_c <N:
                if visited[new_r][new_c] or islands[new_r][new_c] == i:
                    continue
                if islands[new_r][new_c] != 0:
                    return cur_steps
                new_steps = cur_steps+1
                if new_steps >= ans:
                    continue
                q.append((new_r,new_c, new_steps))
                visited[new_r][new_c] = True
    return N**2
    

visited = [[False]*N for _ in range(N)]
island_number = 1
for r in range(N):
    for c in range(N):
        if visited[r][c] or islands[r][c] == 0:
            continue
        border_set = set()
        make_border_set(r,c,island_number)
        islands_borders.append(border_set)
        island_number += 1


ans = N**2 # 최대 거리 N*N

for i in range(len(islands_borders)):
    cur_border_set = islands_borders[i]
    for border_coord in cur_border_set:
        r, c = border_coord
        ans = min(ans, min_bridge_length(r,c,i+1))

print(ans)
