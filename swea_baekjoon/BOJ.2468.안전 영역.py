from collections import deque

N = int(input())
heights = [list(map(int,input().split())) for _ in range(N)]

ans = 1
unflooed = set()
heights_dict = {}
directions = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(coord):
    global safe_zone
    q = deque()
    q.append(coord)
    visited_set.add(coord)
    
    while q:
        cur_r, cur_c = q.popleft()
        for dr, dc in directions:
            new_r, new_c = cur_r+dr, cur_c +dc
            new_coord = (new_r, new_c)
            if 0<=new_r<N and 0<=new_c<N:
                if new_coord not in visited_set and new_coord in unflooed:
                    q.append(new_coord)
                    visited_set.add(new_coord)
    safe_zone += 1
    


for r in range(N):
    for c in range(N):
        height = heights[r][c]
        if not heights_dict.get(height):
            heights_dict[height] = [(r,c)]
        else:
            heights_dict[height].append((r,c))
        unflooed.add((r,c))

# print(len(unflooed))
# print(heights_dict)

flooed_h = 0
while unflooed != set():
    flooed_h += 1
    # print('--------------', flooed_h)
    if not heights_dict.get(flooed_h):
        continue
    flooed_coords = heights_dict[flooed_h]
    # print(flooed_coords)
    for flooed in flooed_coords:
        unflooed.remove(flooed)
    # print(len(unflooed))
    
    safe_zone = 0
    visited_set = set()
    for unflooed_coord in unflooed:
        if unflooed_coord not in visited_set:
            bfs(unflooed_coord)
            # print(visited_set)
    ans = max(ans, safe_zone)

print(ans)
