
from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    end, start = map(int,input().split())
    graph[start].append(end)

def bfs(node):
    q = deque()
    q.append(node)
    visited = [False] *(N+1)
    visited[node] = True
    cnt = 1
    
    while q:
        cur_node = q.popleft()
        for next_node in graph[cur_node]:
            if visited[next_node]:
                continue
            q.append(next_node)
            visited[next_node] = True
            cnt += 1
    return cnt

max_cnt = 0
max_list = []

for i in range(1, 1+N):
    if graph[i] == []:
        cnt = 1
    else:
        cnt = bfs(i)
    
    if max_cnt < cnt:
        max_cnt = cnt
        max_list = [i]
    elif max_cnt == cnt:
        max_list.append(i)
        
print(*max_list)
