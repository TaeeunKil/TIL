# import sys
# sys.stdin = open("input.1267.txt", "r")

T = 10

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))
    adj_out = [[0]*V for _ in range(V)]
    adj_in = [[0]*V for _ in range(V)]
    visited = [0]*V
    for s, e in zip(edges[::2], edges[1::2]):
        adj_out[s-1][e-1] = 1
        adj_in[e-1][s-1] = 1
    
    bfs_list = []
    for i, incoming in enumerate(adj_in):
        if not 1 in incoming:
            bfs_list.append(i)

    def bfs(bfs_list):
        while bfs_list != []:
            n = len(bfs_list)
            for _ in range(n):
                node = bfs_list.pop(0)
                visited[node] = 1 
                print(node+1, end=' ')

                for i, adj in enumerate(adj_out[node]):
                    if adj == 1 and not visited[i]:
                        adj_in[i][node] = 0
                        if not 1 in adj_in[i]:
                            bfs_list.append(i)
                            

    print(f'#{tc}', end= ' ')
    bfs(bfs_list)
    print()