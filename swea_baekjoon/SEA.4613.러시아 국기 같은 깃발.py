T = int(input())
W, B, R = 0, 1, 2
colors = ["W", "B", "R"]


def get_diff(cur_r, target):
    global M
    cnt = 0

    for col in range(M):
        if graph[cur_r][col] != target:
            cnt += 1
    return cnt


def coloring(cur_r, cnt, color_idx, txt):
    global N, M, answer
    if cnt > answer:
        return
    if cur_r == N-1:  # 마지막 줄 도착했으면 카운팅하기 전에 종료하기.
        if "B" not in txt:
            return
        cnt += get_diff(cur_r, "R")
        answer = min(cnt, answer)
        return
    
    
    for ci in range(color_idx, len(colors)):
        current_cost = get_diff(cur_r, colors[ci])
        coloring(cur_r + 1, cnt+current_cost, ci, txt+colors[ci])



for t in range(1, T+1):
    N, M = map(int, input().strip().split())  # row, col
    graph = [list(input().strip()) for _ in range(N)]
    answer = int(1e9)

    initial = get_diff(0, "W")
    coloring(1, initial, 0, "W") # 1번째 줄부터 시작

    print(f"#{t} {answer}")

