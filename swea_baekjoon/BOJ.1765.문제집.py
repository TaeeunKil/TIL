from heapq import heappop, heappush

N, M = map(int, input().split())

degrees = [0]*(N+1)

edges = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int,input().split())
    degrees[e] += 1
    edges[s].append(e)

h = []

for i in range(1, N+1):
    if degrees[i] == 0:
        heappush(h, i)
result = []

while h:
    cur_node = heappop(h)
    result.append(cur_node)
    
    for next_node in edges[cur_node]:
        degrees[next_node] -= 1
        if degrees[next_node] == 0:
            heappush(h, next_node)

print(*result)

