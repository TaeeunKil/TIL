T = int(input())

def cross_point(cross_start, cross_end):
    global ans
    # 기존 연결 선들과 비교
    for line in lines:
        line_start, line_end = line
        # 스타트랑 엔드랑 교차할 조건은
        # 시작점이 위면 끝점이 아래 or 시작점이 아래면 끝점이 위
        if line_start > cross_start and line_end < cross_end:
            ans += 1
        elif line_start < cross_start and line_end > cross_end:
            ans +=1
    lines.append((cross_start,cross_end))

for tc in range(1, T+1):
    ans = 0
    lines = []
    N = int(input())
    for _ in range(N):
        start, end= map(int,input().split())
        cross_point(start, end)
    print(f'#{tc}', ans)