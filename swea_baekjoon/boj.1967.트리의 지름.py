import sys
sys.setrecursionlimit(10**6)

n = int(input())

adj_list = [[] for _ in range(n+1)]        # 부모를 인덱스로 자식을 담고있는 리스트
weighted = [0]*(n+1)         # 자식을 인덱스로 부모와 연결된 가치를 저장

for _ in range(n-1):
    p, c, w = map(int, input().split())
    adj_list[p].append(c)
    weighted[c] = w

ans = 0

def postorder_traversal(node):
    child_list = adj_list[node]
    global ans
    if child_list != []:
        w_list = []
        for child in child_list:
            cur = postorder_traversal(child)
            w_list.append(cur)
        w_list.sort(reverse=True)
        ans = max(ans, sum(w_list[0:2]))
        return max(w_list) + weighted[node]
    else:
        return weighted[node]

root = 1 # 문제에서 선언
postorder_traversal(root)

print(ans)