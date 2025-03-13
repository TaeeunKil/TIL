from heapq import heappop, heappush
import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
tc = 0
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def dijkstra(matrix, start_coord = (0,0)):
    q = []
    visited = [[0]*N for _ in range(N)]
    heappush(q, (matrix[0][0], start_coord))
    visited[0][0] = 1
    
    while q:
        cost, cur_coord = heappop(q)
        cur_r, cur_c = cur_coord
        for dir in range(len(dr)):
            new_r = cur_r + dr[dir]
            new_c = cur_c + dc[dir]
            if 0 <= new_r < N and 0<= new_c < N and not visited[new_r][new_c]:
                if new_r == N-1 and new_c == N-1:
                    return cost + matrix[new_r][new_c]
                heappush(q, (cost + (matrix[new_r][new_c]), (new_r, new_c)))
                visited[new_r][new_c] = 1


while N:
    tc += 1
    maze = [list(map(int, input().split())) for _ in range(N)]
    ans = dijkstra(maze)
    print(f'Problem {tc}: {ans}')
    N = int(input())



# q = []
# heappush(q, 14)
# print(q)