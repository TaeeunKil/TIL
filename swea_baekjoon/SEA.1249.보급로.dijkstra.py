from heapq import heappop, heappush

directions = [(1,0),(0, 1),(-1,0),(0, -1)]

def dijkstra(node):
    q = []
    visited = set()
    sum_times = 0
    heappush(q, (sum_times, node))
    visited.add(node)
        
    while q:
        cur_sum_times, cur_node = heappop(q)
        cur_r, cur_c = cur_node
        for dr, dc in directions:
            new_r, new_c = cur_r + dr, cur_c + dc
            new_node = (new_r, new_c)
            if 0<= new_r<N and 0<=new_c<N:
                if new_node not in visited:
                    visited.add(new_node)
                    new_sum_time = ground[new_r][new_c] + cur_sum_times
                    heappush(q, (new_sum_time, new_node))
                    if new_node == (N-1, N-1):
                        return new_sum_time

    return -1

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ground = [list(map(int, list(input()))) for _ in range(N)]
    ans = 0
    start = (0,0)
    ans = dijkstra(start)
    print(f'#{tc}', ans)