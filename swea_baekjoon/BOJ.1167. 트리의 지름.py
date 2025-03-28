from collections import deque

# 노드 개수
v = int(input())
adj_list = [[] for _ in range(v+1)]

for _ in range(v):
    edges = list(map(int, input().split()))
    start = edges.pop(0)
    edges.pop()  # -1 제거
    num_edges = len(edges)//2
    
    for i in range(num_edges):
        end_idx = 2*i
        end = edges[end_idx]
        weight_idx = 2*i + 1
        weight = edges[weight_idx]
        adj_list[start].append((end, weight))

def bfs(start):
    visited = [0]*(v+1)
    q = deque()  # (현재 노드, 현재까지 거리)
    q.append((start, 0))
    visited[start] = 1
    max_node = start
    max_dist = 0

    while q:
        cur_node, cur_dist = q.popleft()
        if cur_dist > max_dist:
            max_dist = cur_dist
            max_node = cur_node
        for next_node, next_dist in adj_list[cur_node]:
            if not visited[next_node]:
                visited[next_node] = 1
                q.append((next_node, cur_dist + next_dist))
    return max_node, max_dist


start_node, start_dist = bfs(1)
end_node, ans = bfs(start_node)

print(ans)
