class FenwickTree:
    def __init__(self, nodes):
        self.n = len(nodes)
        self.tree = [0] * (self.n+1)
        for i in range(1, self.n+1):
            self.update(i, nodes[i-1]) 
            # 0-based를 1-based로 사용
        
    def update(self, node, delta):
        i = node
        while i <= self.n:
            self.tree[i] += delta
            i += i &-i
            
    def query(self, node):
        result = 0
        i = node
        while i > 0:
            result += self.tree[i]
            i -= i&-i
        return result
    # 펜윅의 쿼리는 1~node 까지의 구간합을 반환한다
    def range_query(self, left, right):
        return self.query(right) - self.query(left-1)


N, M = map(int,input().split())

leaf_nodes = list(map(int,input().split()))

tree = FenwickTree(leaf_nodes)

for _ in range(M):
    left, right = map(int, input().split())
    print(tree.range_query(left, right))