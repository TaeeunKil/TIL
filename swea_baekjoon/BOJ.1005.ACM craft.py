from heapq import heappop, heappush
T = int(input())

for tc in range(T):

    N, K = map(int, input().split())

    degrees = [0]*(N+1)

    edges = [[] for _ in range(N+1)]

    D = [0] + list(map(int, input().split()))

    for _ in range(K):
        s, e = map(int,input().split())
        degrees[e] += 1
        edges[s].append(e)

    W = int(input())

    h = []

    for i in range(1, N+1):
        if degrees[i] == 0:
            heappush(h, (D[i], i))

    while h:
        cur_time, cur_node = heappop(h)
        
        if cur_node == W:
            print(cur_time)
            break
        
        for next_node in edges[cur_node]:
            degrees[next_node] -= 1
            if degrees[next_node] == 0:
                heappush(h, (cur_time+D[next_node], next_node))
