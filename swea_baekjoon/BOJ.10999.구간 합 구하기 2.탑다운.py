class SegmentTreeBottomUp:
    def __init__(self, leaf_nodes):
        self.n = len(leaf_nodes)
        self.tree = [0]*(4*self.n)
        self.lazy = [0]*(4*self.n)
        self.build(1, 0, self.n -1) # 최초의 제작
    
    def plus(self, a, b):
        return a+b
    
    def build(self, node, start, end):
        if start == end:
            self.tree[node] = leaf_nodes[start]
            return
        mid = (start+end) // 2
        self.build(2*node, start, mid)
        self.build(2*node+1, mid+1, end)
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
        
    def propagate(self, node, start, end):
        if self.lazy[node]:
            self.tree[node] += (end - start +1) * self.lazy[node]
            # lazy가 남아있는 놈은 무조건 해당 구간 전부에 lazy값을 적용 하려는 놈
            
            if start != end:
                self.lazy[2*node] += self.lazy[node]
                self.lazy[2*node+1] += self.lazy[node]
            self.lazy[node] = 0
            

    # start, end 는 해당 노드가 감싸고 있는 구간의 양 끝
    # left, right 는 우리가 검색을 원하는 구간의 양 끝
    def query(self, node, start, end, left, right):
        # 검색 중에 만나면 전파부터 해라(그래야 안 꼬임)
        self.propagate(node, start, end)
        
        # 우리가 찾는 구간의 오른쪽이, 해당 노드의 왼쪽보다 작으면 노해당
        # 우리가 찾는 구간의 왼쪽이, 해당 노드의 오른쪽보다 크면 노해당
        if right < start or left > end:
            return 0
        
        # 해당 노드의 범위가 우리가 찾는 범위의 안쪽이면 그 값으로 돌아가라
        if right >= end and left <= start:
            return self.tree[node]
        
        mid = (start+end) //2
        
        return self.query(2*node, start, mid, left, right) + self.query(2*node+1, mid+1, end, left, right)

    def update_range(self, node, start, end, left, right, delta):
        # 업데이트 하러 가다 보이면 전파부터 해라!
        self.propagate(node, start, end)
        
        if right < start or left >end:
            return
        
        if right >= end and left <= start:
            self.lazy[node] += delta
            self.propagate(node, start, end)
            return
        
        mid = (start+end)//2
        self.update_range(2*node, start, mid, left, right, delta)
        self.update_range(2*node+1, mid+1,end, left, right, delta)
        self.tree[node] = self.tree[node*2] + self.tree[node*2+1]
        return


N, M, K = map(int,input().split())


leaf_nodes = [int(input()) for _ in range(N)]
tree = SegmentTreeBottomUp(leaf_nodes)

for _ in range(M+K):
    order = list(map(int,input().split()))
    a= order[0]
    # idx화 하려면 -1 해야한다. 번째의 의미
    b = order[1]-1
    c = order[2]-1
    if a == 1:
        d = order[3]
        tree.update_range(1,0,N-1,b,c,d)

    elif a == 2:
        print(tree.query(1, 0, N-1, b, c))