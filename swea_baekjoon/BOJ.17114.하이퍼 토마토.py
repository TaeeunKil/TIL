from collections import deque

def compute_strides(dims):
    """
    dims: [d0, d1, d2, ..., d_{k-1}] (마지막 차원이 가장 빨리 변한다고 가정)
    반환: 각 차원에 대한 stride 리스트
      예) dims = [d0, d1, d2] -> strides = [d1*d2, d2, 1]
    """
    n = len(dims)
    strides = [0]*n
    strides[-1] = 1
    for i in range(n - 2, -1, -1):
        strides[i] = strides[i + 1] * dims[i + 1]
    return strides

def index_to_coord(index, dims, strides):
    """1차원 인덱스 -> 다차원 좌표"""
    coord = []
    for s in strides:
        c = index // s
        coord.append(c)
        index %= s
    return coord

def coord_to_index(coord, strides):
    """다차원 좌표 -> 1차원 인덱스"""
    return sum(c * s for c, s in zip(coord, strides))

def solve():
    # 1) 첫 줄에 각 차원을 입력받는다 (문제에서 m, n, o, p, q, r, s, t, u, v, w 순)
    dims = list(map(int, input().split()))
    
    # 2) 문제 입력은 "첫 번째 숫자(m)가 가장 빨리 변한다" → 파이썬 BFS 기준과 반대
    #    → 차원 순서를 뒤집어서, "마지막 숫자가 가장 빨리 변한다" 형태로 바꾼다.
    dims.reverse()  
    
    # 3) 전체 셀(토마토)의 개수 = 모든 차원의 곱
    total = 1
    for d in dims:
        total *= d
    
    # 4) 토마토 상태를 읽는다 (총 total개)
    tokens = []
    while len(tokens) < total:
        tokens.extend(input().split())
    tomatoes = list(map(int, tokens[:total]))
    
    # 5) strides 계산
    strides = compute_strides(dims)
    
    # 6) BFS 준비
    days = [-1]*total  # 일수 기록 (익지 않았으면 -1)
    queue = deque()
    
    # 처음부터 익어있는 토마토(1)는 모두 queue에 넣고, days=0으로 설정
    for i in range(total):
        if tomatoes[i] == 1:
            days[i] = 0
            queue.append(i)
    
    # 7) BFS 진행
    while queue:
        cur_idx = queue.popleft()
        cur_coord = index_to_coord(cur_idx, dims, strides)
        cur_day = days[cur_idx]
        
        # 각 차원별로 +/- 1
        for dim_idx in range(len(dims)):
            for delta in (1, -1):
                new_coord = cur_coord[:]
                new_coord[dim_idx] += delta
                # 범위 체크
                if not (0 <= new_coord[dim_idx] < dims[dim_idx]):
                    continue
                
                nxt_idx = coord_to_index(new_coord, strides)
                # 아직 익지 않은 토마토(0)이고, 방문(익기) 기록이 없으면
                if tomatoes[nxt_idx] == 0 and days[nxt_idx] == -1:
                    days[nxt_idx] = cur_day + 1
                    queue.append(nxt_idx)
    
    # 8) 아직 익지 않은 토마토가 남아 있으면 -1
    for i in range(total):
        if tomatoes[i] == 0 and days[i] == -1:
            print(-1)
            return
    
    # 9) 모두 익었다면 익는 데 걸리는 시간의 최댓값
    print(max(days))

if __name__ == '__main__':
    solve()
