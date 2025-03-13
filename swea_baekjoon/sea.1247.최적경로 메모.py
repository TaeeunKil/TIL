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
    full_mask = (1 << N) - 1  # 모든 중간 노드를 방문했을 때의 상태

    def dfs_no_return(current, mask):
        """
        (current, mask) 상태에서의 최소 비용을 dp[current][mask]에 저장.
        별도의 return 없이, dp 테이블을 직접 갱신하는 방식.
        """
        # 이미 계산된 상태라면 바로 종료
        if dp[current][mask] != -1:
            return

        # 모든 노드를 방문한 경우
        if mask == full_mask:
            # 시작점이 (예: 1)이라고 가정했다면, current에서 1로 돌아가는 비용
            dp[current][mask] = adj_matrix[current][1]
            return

        best = float('inf')
        for i in range(N):
            # i번째 노드를 방문하지 않았다면
            if not (mask & (1 << i)):
                next_node = i + 2   # 예: i 노드가 실제 index로는 i+2라고 가정
                new_mask = mask | (1 << i)
                # 자식 상태가 계산 안 되어 있으면 먼저 재귀 호출
                if dp[next_node][new_mask] == -1:
                    dfs_no_return(next_node, new_mask)

                cost = adj_matrix[current][next_node] + dp[next_node][new_mask]
                best = min(cost, best)

        dp[current][mask] = best
    dfs_no_return(0, 0)
    print(f'#{tc}', dp[0][0])
