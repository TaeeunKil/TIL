from heapq import heappop, heappush

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(E):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int,input().split())
# essential path node

def dijkstra(graph, start, end):
    distances = [float('inf') for _ in range(N+1)]
    distances[start] = 0
    hq = [(0, start)]

    while hq:
        cur_dist, cur_node = heappop(hq)

        if cur_node == end:
            return cur_dist

        if cur_dist > distances[cur_node]:
            continue

        for next_node, next_dist in graph[cur_node]:
            new_dist = next_dist + cur_dist
            
            if new_dist < distances[next_node]:
                distances[next_node] = new_dist
                heappush(hq, (new_dist, next_node))
    
    return float('inf')


start1 = dijkstra(graph, 1, v1)
start2 = dijkstra(graph, 1, v2)
v1_to_v2 = dijkstra(graph, v1, v2)
end1 = dijkstra(graph, v1, N)
end2 = dijkstra(graph, v2, N)

ans = min(start1+v1_to_v2+end2,start2+v1_to_v2+end1)

if ans == float('inf'):
    ans = -1

print(ans)