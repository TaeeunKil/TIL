## 1차원 펜윅부터 구현해서 확장함


class FenwickTree2D:
    def __init__(self, matrix):
        self.n = len(matrix)
        self.tree = [[0] * (self.n+1) for _ in range(self.n+1)]
        for i in range(1, self.n+1):
            for j in range(1, self.n+1):
                self.update(i, j, matrix[i-1][j-1]) # 0based를 1based로 사용해야함
        
    def update(self, r, c, delta):
        i = r
        while i <= self.n:
            j = c
            while j <= self.n:
                self.tree[i][j] += delta
                j += j&-j
            i += i &-i
            
    def query(self, r, c):
        res = 0
        i = r
        while i > 0:
            j = c
            while j> 0:
                res += self.tree[i][j]
                j -= j&-j
            i-= i&-i
        return res
    
    def range_query(self, x1, y1, x2, y2):
        return self.query(x2, y2) - self.query(x2, y1-1) - self.query(x1-1, y2) + self.query(x1-1, y1-1)       


N, M = map(int,input().split())

leaf_matrix = [list(map(int,input().split())) for _ in range(N)]

tree = FenwickTree2D(leaf_matrix)

for _ in range(M):
    order = list(map(int,input().split()))
    x1, y1, x2, y2 = order[0], order[1], order[2], order[3]
    print(tree.range_query(x1, y1, x2, y2))
        
        
        
        
        
        
        

