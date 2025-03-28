N = 5
princesses = [list(input()) for _ in range(N)]
directions = [(1,0), (0,-1), (-1,0), (0,1)]

def dfs(r, c, cnt, candidate, ys):
    global ans
    
    if cnt == 7:
        if ys.count('S') >= 4:
            # print(r,c,ys)
            # print(visited)
            # print('-------')
            ans += 1
        return
    
    if ys.count('Y') >= 4:
        return
    
    new_candidate = candidate.copy()
    new_candidate.remove((r,c))
    
    for dr, dc in directions:
        nr, nc = r+dr, c+dc       
        if 0<=nr<N and 0<=nc<N:
            if (nr, nc) not in visited:
                new_candidate.add((nr,nc))

    
    for nr, nc in new_candidate:
        if (nr,nc) not in visited:
            visited.add((nr,nc))
            checking_set = frozenset(visited)
            if checking_set not in checked:
                checked.add(checking_set)
                dfs(nr,nc,cnt+1, new_candidate, ys+princesses[nr][nc])
            visited.remove((nr,nc))


ans = 0

dasom = []
for r in range(N):
    for c in range(N):
        if princesses[r][c] == 'S':
           dasom.append((r,c))

checked = set()
for r, c in dasom:
    visited = set()
    visited.add((r,c))
    dfs(r, c, 1, {(r,c)}, princesses[r][c])
    visited.remove((r,c))

print(ans)