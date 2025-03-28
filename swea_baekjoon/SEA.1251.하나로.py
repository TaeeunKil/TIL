from heapq import heappop, heappush

def dijkstra(node):
    q = []
    visited = [False] *(N)
    fee = 0
    sum_fee = 0
    heappush(q, (fee, node))
        
    while q:
        cur_fee, cur_node = heappop(q)
        if not visited[cur_node]:
            visited[cur_node] = True
            sum_fee += cur_fee
            for adj_node in range(N):
                if adj_node == cur_node or visited[adj_node]:
                    continue
                connect_fee = adj_matrix[cur_node][adj_node]
                heappush(q, (connect_fee, adj_node))

    return sum_fee

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    adj_matrix = [[-1]*N for _ in range(N)]
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())
    for i in range(N):
        for j in range(i,N):
            L_square = abs(x_list[i] - x_list[j])**2 + abs(y_list[i]-y_list[j])**2
            environmental_fee = E*L_square
            adj_matrix[i][j] = environmental_fee
            adj_matrix[j][i] = environmental_fee
    print(f'#{tc}', round(dijkstra(0)))