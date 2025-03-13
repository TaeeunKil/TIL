from collections import deque


M, N= map(int, input().split())
real_ans = 0
box = [list(map(int, input().split())) for _ in range(N)]

direction = [(1,0), (0,1), (0,-1), (-1,0)]

def ripen_bfs(matrix):
    if all(0 not in row for row in matrix):
        return 0
    ans =-1
    while q:
        l = len(q)
        for _ in range(l):
            cur_i, cur_j = q.popleft()
            for di, dj in direction:                
                new_i, new_j = cur_i+di, cur_j+dj
                if 0<=new_i<N and 0<=new_j<M:
                    if matrix[new_i][new_j] == 0:
                        matrix[new_i][new_j] = 1
                        q.append((new_i, new_j))
                        
        ans +=1
    if any(0 in row for row in matrix):
        return -1
    return ans

q = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i,j))

print(ripen_bfs(box))