import sys
from array import array

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

mod = 10**9+7 # 모듈러 연산으로 해야함함

class SegmentTreeBottomUp:
    def __init__(self, leaf_nodes):
        self.n = len(leaf_nodes)
        self.tree = array('I', [1]*(4*self.n))
        self.build(1, 0, self.n -1) # 최초의 제작
    
    def build(self, node, start, end):
        if start == end:
            self.tree[node] = leaf_nodes[start]%mod
            return
        mid = (start+end) // 2
        self.build(2*node, start, mid)
        self.build(2*node+1, mid+1, end)
        self.tree[node] = (self.tree[2*node] * self.tree[2*node+1]) % mod

    
    # start, end 는 해당 노드가 감싸고 있는 구간의 양 끝
    # left, right 는 우리가 검색을 원하는 구간의 양 끝
    def query(self, node, start, end, left, right):
        
        # 우리가 찾는 구간의 오른쪽이, 해당 노드의 왼쪽보다 작으면 노해당
        # 우리가 찾는 구간의 왼쪽이, 해당 노드의 오른쪽보다 크면 노해당
        if right < start or left > end:
            return 1
        
        # 해당 노드의 범위가 우리가 찾는 범위의 안쪽이면 그 값으로 돌아가라
        if right >= end and left <= start:
            return self.tree[node]
        
        mid = (start+end) //2
        
        return (self.query(2*node, start, mid, left, right) * self.query(2*node+1, mid+1, end, left, right))%mod

    def update_one(self, node, start, end, idx, delta):
        
        if idx > end or idx < start:
            return
        
        self.tree[node] = (self.tree[node] * delta)%mod
        
        if start != end:
            mid = (start+end)//2
            self.update_one(2*node, start, mid, idx, delta)
            self.update_one(2*node+1, mid+1,end, idx, delta)

    def rebuild(self, node, start, end, idx, c):

        if idx > end or idx < start:
            return
        
        if start == end:
            self.tree[node] = c
            return
        mid = (start+end) // 2
        if idx <= mid: #왼쪽
            self.rebuild(2*node, start, mid, idx, c)
        else: # 오른쪽
            self.rebuild(2*node+1, mid+1, end, idx, c)
        # 하나만 했으면 좋겠다다
        self.tree[node] = (self.tree[2*node] * self.tree[2*node+1])%mod

N, M, K = map(int,input().split())

leaf_nodes = array('I', (int(sys.stdin.readline()) for _ in range(N)))


tree = SegmentTreeBottomUp(leaf_nodes)

for _ in range(M+K):
    a, b, c = map(int,input().split())
    # idx화 하려면 -1 해야한다. 번째의 의미
    b -= 1
    if a == 1:
        c %= mod
        if c == leaf_nodes[b]:
            continue
        elif leaf_nodes[b] == 0:
            tree.rebuild(1, 0, N-1, b, c)
            continue
        delta = c * pow(leaf_nodes[b], mod-2, mod) % mod
        leaf_nodes[b] = c
        tree.update_one(1, 0, N-1, b, delta)
    elif a == 2:
        c -= 1
        print(int(tree.query(1, 0, N-1, b, c)%mod))