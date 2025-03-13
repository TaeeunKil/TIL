
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    # 도착점에 도달하면 1을 반환
    if x == N-1 and y == M-1:
        return 1
    
    # 이미 방문한 적 있다면 그 값을 바로 반환
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0  
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 범위 내에 있고, 현재 위치보다 낮은 곳으로 이동할 때만 진행
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] < graph[x][y]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]

# (0,0)에서 출발하는 경로의 개수 출력
print(dfs(0, 0))
