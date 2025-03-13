from itertools import combinations
from pprint import pprint as print
from collections import deque

N = int(input())

population = list(map(int, input().split()))



adj_matrix = [[0]*N for _ in range(N)]

for s in range(N):
    for i, e in enumerate(map(int, input().split())):
        if i == 0:
            continue
        adj_matrix[s][e-1] = 1


def bfs(start):
    isblue = area_blue[start]
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        s = q.popleft()
        for i, e in enumerate(adj_matrix[s]):
            if i == s:
                continue
            if e == 1:
                if area_blue[i] == isblue and not visited[i]:
                    q.append(i)
                    visited[i] = 1



ans = float('inf')

for i in range(1,N):
    for comb in combinations(range(N), i):
        visited = [0]*N
        area_blue = [0]*N
        for blue in comb:
            area_blue[blue] = 1
        bfs(area_blue.index(0))
        bfs(area_blue.index(1))
        if visited == [1]*N:
            blue = 0
            red = 0
            for j in range(N):
                if area_blue[j] == 1:
                    blue += population[j]
                else:
                    red += population[j]
            ans = min(ans, abs(blue-red))

if ans == float('inf'):
    ans = -1
                
print(ans)

