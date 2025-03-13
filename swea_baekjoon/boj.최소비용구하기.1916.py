import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

# 도시 번호가 1부터 시작하므로 (N+1) 크기의 리스트 생성
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

distance = [float('inf')] * (N+1)
distance[start] = 0

heap = []
heapq.heappush(heap, (0, start))

while heap:
    cur_cost, cur_city = heapq.heappop(heap)
    if cur_cost > distance[cur_city]:
        continue

    for next_city, cost in graph[cur_city]:
        new_cost = cur_cost + cost
        if new_cost < distance[next_city]:
            distance[next_city] = new_cost
            heapq.heappush(heap, (new_cost, next_city))

print(distance[end])