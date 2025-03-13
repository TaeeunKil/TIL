
def make_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    xy = list(map(int, input().split()))
    num_points = N + 2  # 0: 시작, 1: 끝, 2~N+1: 중간 지점들

    # 인접 행렬 구성 (맨해튼 거리)
    adj_matrix = [[0] * num_points for _ in range(num_points)]
    for i in range(num_points):
        x1, y1 = xy[2*i], xy[2*i+1]
        for j in range(num_points):
            if i == j:
                continue
            x2, y2 = xy[2*j], xy[2*j+1]
            adj_matrix[i][j] = make_distance(x1, y1, x2, y2)

    # dp[current][mask]: 현재 노드(current)에서 mask에 해당하는 중간 노드들을 방문한 상태일 때,
    # 남은 경로를 포함한 최소 비용.
    # 중간 노드는 2번부터 N+1번까지 있으므로, mask의 크기는 N (비트 0~N-1 사용; i번째 비트는 노드 i+2 방문 여부)
    dp = [[-1] * (1 << N) for _ in range(num_points)]
    print(dp)
    full_mask = (1 << N) - 1  # 모든 중간 노드를 방문했을 때의 상태
    print(bin(full_mask))

    def dfs(current, mask):
        # 모든 중간 노드를 방문했으면, 현재 노드에서 끝 노드(1)로 가는 비용을 반환
        if mask == full_mask:
            return adj_matrix[current][1]
        # 이미 계산된 상태이면 바로 반환 (메모이제이션)
        if dp[current][mask] != -1:
            return dp[current][mask]
        best = float('inf')
        # 아직 방문하지 않은 중간 노드(인덱스 i, 글로벌 노드 번호 i+2)에 대해 재귀적으로 탐색
        for i in range(N):
            if ((mask >> i) & 1) == 0: # mask의 i 번째 비트가 0인지
                next_node = i + 2
                new_mask = mask | (1 << i)
                cost = adj_matrix[current][next_node] + dfs(next_node, new_mask)
                best = min(best, cost)
        dp[current][mask] = best  # 해당 상태에 대한 최소 비용 저장
        return best

    ans = dfs(0, 0)
    print(f'#{tc}', ans)
