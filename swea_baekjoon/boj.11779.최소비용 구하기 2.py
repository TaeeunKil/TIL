from heapq import heappop, heappush

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

s, e = map(int,input().split())

def dijkstra(graph, start, end):
    costs = [float('inf') for _ in range(n+1)]
    costs[start] = 0
    hq = [(0, start, [start])]

    while hq:
        cur_cost, cur_node, cur_path = heappop(hq)

        if cur_node == end:
            break 

        if cur_cost > costs[cur_node]:
            continue

        for next_node, next_dist in graph[cur_node]:
            new_cost = next_dist + cur_cost
            
            if new_cost < costs[next_node]:
                costs[next_node] = new_cost
                new_path = cur_path + [next_node]
                heappush(hq, (new_cost, next_node, new_path))
    
    return cur_cost, cur_path


ans_cost, ans_path = dijkstra(graph, s, e)
print(ans_cost)
print(len(ans_path))
print(*ans_path)
