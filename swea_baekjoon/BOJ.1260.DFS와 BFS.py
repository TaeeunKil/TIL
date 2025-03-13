
N, M, V = map(int, input().split())
matrix_adj = [[0]*N for _ in range(N)]
for _ in range(M):
    i, j= map(int, input().split())
    matrix_adj[i-1][j-1] = 1
    matrix_adj[j-1][i-1] = 1
    
def dfs(V,c=0, visited = [0]*N):
    if c == N:
        return
    
    print(V, end=' ')
    visited[V-1] = 1
    for i, adj in enumerate(matrix_adj[V-1]):
        if adj == 1 and not visited[i]:
             dfs(i+1, c+1, visited)   
    # for i in range(N):
    #     if not visited[i] and matrix_adj[V-1][i] == 1:
    #         dfs(i)


dfs(V)
print()

def bfs(V):
    visited = [0]*N
    bfs_list=[V]
    visited[V-1] = 1

    while bfs_list != []:
        node = bfs_list.pop(0)
        print(node, end=' ')
        
        for i, adj in enumerate(matrix_adj[node-1]):
            if adj == 1 and not visited[i]:
                bfs_list.append(i+1)
                visited[i] = 1
bfs(V)

# visited = [0]*(N+1)
# from collections import deque #덱
# def bfs_deque(v):
#     q = deque()
#     print(v, end= ' ')
#     visited[v] = 2
#     q.append(v)
#     # q가 빌때까지 돈다
#     while q:
#         cur_pos = q.popleft()
#         for i in range(1, N+1):
#             if matrix_adj[cur_pos][i] == 1 and visited[i] == 1:
#                 print(i, end= ' ')
#                 visited[i] = 2
#                 q.append(i)
## 조심해야하는 것 : 방문처리할 때 bfs는 무조건 넣을 때 해야한다
## 왜냐하면 같은 라인 체크할때 다시 넣을 수 있기 때문에!