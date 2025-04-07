class SegmentMinTree:
    def __init__(self, leaf_nodes):
        self.n = len(leaf_nodes)
        self.inf = float('inf')
        self.tree = [self.inf]*(4*self.n)
        self.build(1, 0, self.n -1) # 최초의 제작
    
    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.leaf_nodes[start]
            return
        mid = (start+end) // 2
        self.build(2*node, start, mid)
        self.build(2*node+1, mid+1, end)
        self.tree[node] = min(self.tree[2*node], self.tree[2*node+1])
        
    def query(self, node, start, end, left, right):
        if right < start or left > end:
            return self.inf

        if right >= end and left <= start:
            return self.tree[node]
        
        mid = (start+end) //2
        
        return min(self.query(2*node, start, mid, left, right), self.query(2*node+1, mid+1, end, left, right))

N, M = map(int,input().split())


leaf_nodes = [int(input()) for _ in range(N)]
tree = SegmentMinTree(leaf_nodes)

for _ in range(M):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    print(tree.query(1, 0, N-1, a, b))
