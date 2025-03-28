import sys
input = sys.stdin.readline

class SegmentTree2D:
    def __init__(self, leaf_matrix):

        self.n = len(leaf_matrix) - 1         # 행의 수는 -1
        self.m = len(leaf_matrix[1]) - 1      # 열의 수도 -1
        self.leaf_matrix = leaf_matrix
        # 2차원 세그먼트 트리: 외부 트리 크기는 4*n, 각 내부 트리 크기는 4*m
        self.tree = [[0]*(4*self.m) for _ in range(4*self.n)]
        self.build_x(1, 1, self.n)
        
    # 외부 트리(행에 대한) 구축 함수
    def build_x(self, node_x, start_x, end_x):
        if start_x == end_x:
            # 외부 노드가 단일 행을 담당하면 해당 행의 내부 세그먼트 트리를 구축
            self.build_y(node_x, start_x, 1, 1, self.m)
        else:
            mid = (start_x + end_x) // 2
            self.build_x(2*node_x, start_x, mid)
            self.build_x(2*node_x+1, mid+1, end_x)
            # 자식 외부 노드의 내부 트리들을 병합하여 현재 외부 노드의 내부 트리 구축
            self.build_y_merge(node_x, 1, 1, self.m)
            
    # 단일 행(row)에 대한 내부 세그먼트 트리 구축 (리프 외부 노드)
    def build_y(self, node_x, row, node_y, start_y, end_y):
        if start_y == end_y:
            self.tree[node_x][node_y] = self.leaf_matrix[row][start_y]
        else:
            mid = (start_y + end_y) // 2
            self.build_y(node_x, row, 2*node_y, start_y, mid)
            self.build_y(node_x, row, 2*node_y+1, mid+1, end_y)
            self.tree[node_x][node_y] = self.tree[node_x][2*node_y] + self.tree[node_x][2*node_y+1]
            
    # 내부 트리 병합: 자식 외부 노드(2*node_x, 2*node_x+1)의 내부 트리 정보를 이용하여 내부 트리 구성
    def build_y_merge(self, node_x, node_y, start_y, end_y):
        if start_y == end_y:
            self.tree[node_x][node_y] = self.tree[2*node_x][node_y] + self.tree[2*node_x+1][node_y]
        else:
            mid = (start_y + end_y) // 2
            self.build_y_merge(node_x, 2*node_y, start_y, mid)
            self.build_y_merge(node_x, 2*node_y+1, mid+1, end_y)
            self.tree[node_x][node_y] = self.tree[2*node_x][node_y] + self.tree[2*node_x+1][node_y]
            
    # 2차원 쿼리: 행 구간 [x1, x2]와 열 구간 [y1, y2]의 합 구하기
    def query_x(self, node_x, start_x, end_x, x1, x2, y1, y2):
        if x2 < start_x or x1 > end_x:
            return 0
        if x1 <= start_x and end_x <= x2:
            return self.query_y(node_x, 1, 1, self.m, y1, y2)
        mid = (start_x + end_x) // 2
        return self.query_x(2*node_x, start_x, mid, x1, x2, y1, y2) + \
               self.query_x(2*node_x+1, mid+1, end_x, x1, x2, y1, y2)
    
    def query_y(self, node_x, node_y, start_y, end_y, y1, y2):
        if y2 < start_y or y1 > end_y:
            return 0
        if y1 <= start_y and end_y <= y2:
            return self.tree[node_x][node_y]
        mid = (start_y + end_y) // 2
        return self.query_y(node_x, 2*node_y, start_y, mid, y1, y2) + \
               self.query_y(node_x, 2*node_y+1, mid+1, end_y, y1, y2)
    
    # 2차원 업데이트: (x, y) 위치의 값을 delta만큼 변경(즉, 기존 값에 delta를 더함)
    def update_x(self, node_x, start_x, end_x, x, y, delta):
        if x < start_x or x > end_x:
            return
        if start_x == end_x:
            self.update_y(node_x, 1, 1, self.m, y, delta)
        else:
            mid = (start_x + end_x) // 2
            if x <= mid:
                self.update_x(2*node_x, start_x, mid, x, y, delta)
            else:
                self.update_x(2*node_x+1, mid+1, end_x, x, y, delta)
            # 자식 외부 노드의 내부 트리 값 변경에 따라 현재 노드의 내부 트리도 갱신
            self.update_y_merge(node_x, 1, 1, self.m, y)
    
    def update_y(self, node_x, node_y, start_y, end_y, y, delta):
        if y < start_y or y > end_y:
            return
        if start_y == end_y:
            self.tree[node_x][node_y] += delta
        else:
            mid = (start_y + end_y) // 2
            if y <= mid:
                self.update_y(node_x, 2*node_y, start_y, mid, y, delta)
            else:
                self.update_y(node_x, 2*node_y+1, mid+1, end_y, y, delta)
            self.tree[node_x][node_y] = self.tree[node_x][2*node_y] + self.tree[node_x][2*node_y+1]
    
    # 내부 트리 병합 업데이트: 내부 노드에서 y에 해당하는 구간만 갱신
    def update_y_merge(self, node_x, node_y, start_y, end_y, y):
        if start_y == end_y:
            self.tree[node_x][node_y] = self.tree[2*node_x][node_y] + self.tree[2*node_x+1][node_y]
        else:
            mid = (start_y + end_y) // 2
            if y <= mid:
                self.update_y_merge(node_x, 2*node_y, start_y, mid, y)
            else:
                self.update_y_merge(node_x, 2*node_y+1, mid+1, end_y, y)
            self.tree[node_x][node_y] = self.tree[2*node_x][node_y] + self.tree[2*node_x+1][node_y]


N, M = map(int, input().split())
# 1-based로 바꿈
leaf_matrix = [[0] + list(map(int, input().split())) for _ in range(N)]
leaf_matrix = [0] + leaf_matrix

tree = SegmentTree2D(leaf_matrix)

for _ in range(M):
    order = list(map(int, input().split()))
    w = order[0]
    if w == 0:
        x, y, c = order[1], order[2], order[3]
        # delta = 새 값 - 기존 값
        delta = c - leaf_matrix[x][y]
        leaf_matrix[x][y] = c
        tree.update_x(1, 1, tree.n, x, y, delta)
    elif w == 1:
        x1, y1, x2, y2 = order[1], order[2], order[3], order[4]
        print(tree.query_x(1, 1, tree.n, x1, x2, y1, y2))
