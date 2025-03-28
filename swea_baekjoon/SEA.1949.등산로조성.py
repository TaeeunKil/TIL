
T = int(input())

directions = [(0,1),(0,-1),(1,0),(-1,0)]

def dfs(r, c, cnt = 1, use_cut_count = False):
    global ans
    cur_height = hiking_trail[r][c]
    visited[r][c] = True
    # print(r, c, cnt, use_cut_count)
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if 0<= nr <N and 0 <= nc < N:
            if visited[nr][nc]:
               continue
            new_height = hiking_trail[nr][nc]
            
            
            if new_height < cur_height:
                dfs(nr, nc, cnt+1, use_cut_count)
            
            elif new_height >= cur_height:
                if not use_cut_count:
                    needed_cut = new_height-cur_height+1
                    if needed_cut <= K:
                        hiking_trail[nr][nc] = new_height - needed_cut
                        dfs(nr, nc, cnt+1, True)
                        hiking_trail[nr][nc] = new_height

    visited[r][c] = False
    if cnt > ans:
        ans = cnt

for tc in range(1, T+1):
    N, K = map(int, input().split())
    hiking_trail = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    visited = [[False] * N for _ in range(N)]
    max_v = 0
    for row in hiking_trail:
        max_v = max(max_v, max(row))
    
    for r in range(N):
        for c in range(N):
            if hiking_trail[r][c] == max_v:
                dfs(r, c)

    print(f'#{tc}', ans)