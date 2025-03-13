from heapq import heappop, heappush
V, E = map(int, input().split())
K = int(input())

graph = {}

distance = [float('inf')]*(V+1)
distance[K] = 0

for i in range(1,V+1):
    graph[i] = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

q = []
heappush(q, (0, K))

while q:
    cur_w, cur_node = heappop(q)
    if distance[cur_node] < cur_w:
        continue
    
    for next_node, weight in graph[cur_node]:
        new_w = cur_w+weight
        if distance[next_node] > new_w:
            distance[next_node] = new_w
            heappush(q, (new_w, next_node))


for i in range(1,V+1):
    if distance[i] == float('inf'):
        print('INF')
        continue
    print(distance[i])