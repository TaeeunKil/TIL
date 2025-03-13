from collections import deque


M, N, H= map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
directions = [(0,1,0), (0,0,1), (0, 0,-1), (0,-1,0), (1, 0, 0), (-1, 0, 0)]

def ripen_bfs(boxes):
    ans = 0
    while q:
        l = len(q)
        for _ in range(l):
            cur_h, cur_i, cur_j, day = q.popleft()
            ans = day
            for dh, di, dj in directions:                
                new_h, new_i, new_j = cur_h+dh, cur_i+di, cur_j+dj
                if 0<=new_i<N and 0<=new_j<M and 0<=new_h<H:
                    if boxes[new_h][new_i][new_j] == 0:
                        boxes[new_h][new_i][new_j] = 1
                        q.append((new_h, new_i, new_j, day+1))
    for floor in boxes:
        if any(0 in row for row in floor):
            return -1
    return ans

q = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if boxes[h][i][j] == 1:
                q.append((h,i,j,0))

print(ripen_bfs(boxes))