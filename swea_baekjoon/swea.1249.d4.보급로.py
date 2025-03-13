
from collections import deque
inf = float('inf')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dist = [[inf] * N for _ in range(N)]
    matrix = [list(map(int, input())) for _ in range(N)]
    dist[0][0] = matrix[0][0] 

    queue = deque()
    queue.append((0, 0))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N:
                new_cost = dist[x][y] + matrix[new_x][new_y]
                if new_cost < dist[new_x][new_y]:
                    dist[new_x][new_y] = new_cost
                    queue.append((new_x, new_y))
    print(f'#{tc} {dist[N-1][N-1]}')