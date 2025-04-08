from heapq import heappop, heappush

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)] 

for i in range(M):
    s, e, T = map(int,input().split())
    graph[s].append((e,T))

def dijkstra(graph, start, end):
    costs = [float('inf') for _ in range(N+1)]
    costs[start] = 0
    hq = [(0, start)]

    while hq:
        cur_cost, cur_node = heappop(hq)

        if cur_node == end:
            break 

        if cur_cost > costs[cur_node]:
            continue

        for next_node, next_cost in graph[cur_node]:
            new_cost = next_cost + cur_cost
            
            if new_cost < costs[next_node]:
                costs[next_node] = new_cost
                heappush(hq, (new_cost, next_node))
    
    return cur_cost

ans = 0
for i in range(1, N+1):
    ans = max(ans, dijkstra(graph, i, X)+dijkstra(graph, X,i))

print(ans)