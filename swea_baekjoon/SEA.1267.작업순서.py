from collections import deque

T = 10

def bfs(node):
    q=deque()
    q.append(node)
    degrees[node] -= 1
    result.append(node)
 
    while q:
        cur_node = q.popleft()
        cur_adj = adj_list[cur_node]

        for next_node in cur_adj:
            degrees[next_node] -= 1
            if degrees[next_node] == 0 and next_node not in result:
                q.append(next_node)
                result.append(next_node)
 
for tc in range(1,T+1):
    V, E=map(int,input().split())
    edges = list(map(int,input().split()))
    degrees = [0]*(V+1)
    adj_list = [[] for _ in range(V+1)]
    result=[]
    zero=[]
    for i in range(0, len(edges)//2):
        start_idx = 2*i
        end_idx = start_idx + 1
        start_node = edges[start_idx]
        end_node = edges[end_idx]
        degrees[end_node] += 1
        adj_list[start_node].append(end_node)

    
    for node in range(1,V+1):
        if degrees[node] == 0:
            zero.append(node)
    
    for node in zero:
        bfs(node)
        
    print(f'#{tc}', *result)
