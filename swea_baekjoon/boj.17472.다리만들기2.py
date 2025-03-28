from collections import deque
from heapq import heappop, heappush


N, M = map(int,input().split())
islands = [list(map(int,input().split())) for _ in range(N)]

directions = [(1,0), (-1,0), (0, 1), (0, -1)]

def labelling(r,c,i):
    q = deque()
    q.append((r,c))
    visited[r][c] = True
    
    while q:
        cur_r, cur_c = q.popleft()
        islands[cur_r][cur_c] = i
        for dr, dc in directions:
            new_r, new_c = cur_r + dr, cur_c + dc
            if 0<= new_r<N and 0<= new_c <M:
                if visited[new_r][new_c] or islands[new_r][new_c] == 0:
                    continue
                q.append((new_r, new_c))
                visited[new_r][new_c] = True

adj_dict = [0]
label = 1
visited = [[False]*M for _ in range(N)]
for r in range(N):
    for c in range(M):
        if islands[r][c] == 1 and not visited[r][c]:
            labelling(r,c,label)
            adj_dict.append({})
            label += 1


for r in range(N):
    start_island = 0
    zero_count = 0
    for c in range(M):
        cur_no = islands[r][c]
        if cur_no == 0:
            zero_count += 1
        else:
            if start_island !=0 and cur_no != start_island and zero_count > 1:
                if adj_dict[start_island].get(cur_no):
                    if adj_dict[start_island][cur_no] > zero_count:
                        adj_dict[start_island][cur_no] = zero_count
                        adj_dict[cur_no][start_island] = zero_count
                else:
                    adj_dict[start_island][cur_no] = zero_count
                    adj_dict[cur_no][start_island] = zero_count
            start_island = cur_no
            zero_count = 0


for c in range(M):
    start_island = 0
    zero_count = 0
    for r in range(N):
        cur_no = islands[r][c]
        if cur_no == 0:
            zero_count += 1
        else:
            if start_island !=0 and cur_no != start_island and zero_count > 1:
                if adj_dict[start_island].get(cur_no):
                    if adj_dict[start_island][cur_no] > zero_count:
                        adj_dict[start_island][cur_no] = zero_count
                        adj_dict[cur_no][start_island] = zero_count
                else:
                    adj_dict[start_island][cur_no] = zero_count
                    adj_dict[cur_no][start_island] = zero_count
            start_island = cur_no
            zero_count = 0


def prim(cost, node):
    pq = []
    heappush(pq, (cost, node))
    visited = [False]*len(adj_dict)
    min_cost = 0
    connected_count = 0
    
    while pq:
        cur_cost, cur_node = heappop(pq)
        
        if visited[cur_node]:
            continue
        
        visited[cur_node] = 1
        min_cost = min_cost + cur_cost
        connected_count += 1
        
        for next_node, next_cost in adj_dict[cur_node].items():
            if visited[next_node]:
                continue
            heappush(pq, (next_cost, next_node))
    
    if connected_count != label -1:
        return -1
    
    return min_cost
            
print(prim(0, 1))