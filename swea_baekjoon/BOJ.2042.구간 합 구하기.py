class SegmentTreeBottomUp:
    def __init__(self, leaf_nodes):
        self.n = len(leaf_nodes)
        self.tree = [0]*(2*self.n)
        self.tree[self.n:] = leaf_nodes[:]
        self.build()
    
    def plus(self, a, b):
        return a+b
    
    def build(self):
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.plus(self.tree[2*i], self.tree[2*i+1])
    
    
    def query(self, left, right):
        left += self.n
        right += self.n
        # 트리의 인덱스로 변형
        result = 0
        while left <= right:
            if left % 2 == 1:
                result = self.plus(result, self.tree[left])
                left +=1
            if right % 2 == 0:
                result = self.plus(result, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
        return result

    def update(self, idx, val):
        i = self.n +idx
        self.tree[i] = val
        while i >= 1:
            i = i //2
            self.tree[i] = self.plus(self.tree[i*2], self.tree[i*2+1])



N, M, K = map(int,input().split())

leaf_nodes = []
for _ in range(N):
    leaf_nodes.append(int(input()))
tree = SegmentTreeBottomUp(leaf_nodes)

for _ in range(M+K):
    a, b, c = map(int,input().split())
    if a == 1:
        tree.update(b-1, c) 
    if a == 2:
        print(tree.query(b-1, c-1))