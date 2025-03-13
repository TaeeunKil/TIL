import sys
sys.stdin = open(r"C:\Users\SSAFY\Desktop\학습\input (4).txt", "r")

T = int(input())
for tc in range(1, T + 1):
    V, E, A, B = map(int, input().split())
    ad = list(map(int, input().split()))
    ad = [x-1 for x in ad] #노드 번호 하나씩 당기기 인덱스로로
    toward_list = {i : [] for i in range(V)}
    incoming_list = {0: 0}
    for a, b in zip(ad[::2], ad[1::2]):
            toward_list[a].append(b)
            incoming_list[b] = a
    sub_tree = [0]*V
    ans_node = -1

    def subtree_dfs(node):

        toward = toward_list[node]

        if toward == []:
             sub_tree[node] = 1
             return 1
        
        count = 1
        for ad in toward_list[node]:
            count += subtree_dfs(ad)
        sub_tree[node] = count
        return count
    
    subtree_dfs(0)


    def tracking(a, b):
         a -= 1
         b -= 1
         ancestor_a =set()
         ancestor_b =set()
         while not ancestor_a & ancestor_b:
            father_a = incoming_list[a]
            father_b = incoming_list[b]
            ancestor_a.add(father_a)
            ancestor_b.add(father_b)
            a = father_a
            b = father_b
         ans_node= list(ancestor_a&ancestor_b)           
         return ans_node[0]
         
    ans_node = tracking(A, B)
    print(f'#{tc} {ans_node+1} {sub_tree[ans_node]}')


    # def dfs(V,c=0, visited = [0]*N):
    #     if c == N:
    #         return
        
    #     print(V, end=' ')
    #     visited[V-1] = 1
    #     for i, adj in enumerate(matrix_adj[V-1]):
    #         if adj == 1 and not visited[i]:
    #             dfs(i+1, c+1, visited)   
        
