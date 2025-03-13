from collections import deque
from pprint import pprint

N, M = map(int, input().split())

iceberg = [list(map(int,input().split())) for _ in range(N)]

directions = [(1,0), (0,1), (-1,0), (0, -1)]

coord_set = set()
adj_dict = {}
mapping = {} # 밸류에 대한 값

def find_first_split():
    global coord_set
    i = 0
    while coord_set != 0:
                        
        i += 1
        remove_set = set()
        for cur_coord, adj_list in adj_dict.items():
            melted_height = mapping[cur_coord][0] - mapping[cur_coord][1]
            if melted_height <= 0:
                remove_set.add(cur_coord)
            else:
                mapping[cur_coord][0] = melted_height
        
        if remove_set == set():
            continue

        coord_set = coord_set - remove_set
        
        if coord_set == set():
            return 0
        
        
        for removed_coord in remove_set:
            del adj_dict[removed_coord]
            del mapping[removed_coord]
            
            for cur_coord, adj_list in adj_dict.items():
                if removed_coord in adj_list:
                    adj_list.remove(removed_coord)
                    mapping[cur_coord][1] += 1
        visited = set()

        for coord in coord_set:
            check_coord = coord
            break

        bfs(check_coord, visited, adj_dict)
        if visited != coord_set:
            break
    return i
                        

def bfs(coord, visited, adjdict):
    
    q = deque()
    q.append(coord)
    visited.add(coord)
    
    while q:
        cur = q.popleft()
        adj_list = adjdict[cur]
        for new_coord in adj_list:
            if new_coord not in visited:
                q.append(new_coord)
                visited.add(new_coord)
         
    return visited
      


for r in range(N):
    for c in range(M):
        cur_position = (r,c)
        height = iceberg[r][c]
        if height == 0:
            continue
        coord_set.add(cur_position)
        mapping[cur_position] = [height, 0]
        if not adj_dict.get(cur_position):
            adj_dict[cur_position] = []
        zeros = 0        
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0<= nr <N and 0<= nc<M:
                if iceberg[nr][nc] == 0:
                    zeros += 1
                    continue
                new_position = (nr, nc)
                adj_dict[cur_position].append(new_position)
        mapping[cur_position][1] = zeros

print(find_first_split())