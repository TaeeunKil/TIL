from collections import deque

N, M = map(int, input().split())
walls = [list(map(int, input())) for _ in range(N)]
visited = [[[0]*M for _ in range(N)] for _ in range(2)]
q = deque()
di = [1, 0, -1, 0]
dj = [0, 1, 0 , -1]

def bfs():
    q.append((0,0,1))
    visited[1][0][0] = 1
    count = 0
    while q:
        count += 1
        for _ in range(len(q)):
            cur_i, cur_j, break_no = q.popleft()

            if cur_i == N-1 and cur_j == M-1:
                return count

            for i in range(len(di)):
                new_i = cur_i + di[i]
                new_j = cur_j + dj[i]
                if 0<= new_i <N and 0<= new_j <M:
                    if walls[new_i][new_j] == 0 and not visited[break_no][new_i][new_j]:
                        q.append((new_i, new_j, break_no))
                        visited[break_no][new_i][new_j] = 1
                    elif walls[new_i][new_j] == 1 and break_no == 1 and not visited[break_no-1][new_i][new_j]:
                        q.append((new_i, new_j, break_no-1))
                        visited[break_no-1][new_i][new_j] = 1
    return -1            

print(bfs())


