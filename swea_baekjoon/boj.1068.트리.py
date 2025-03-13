import sys
input = sys.stdin.readline

n = int(input().strip())
parents = list(map(int, input().split()))
remove = int(input().strip())

tree = [[] for _ in range(n)]
root = -1

#트리 만들기
for i in range(n):
    if parents[i] == -1:
        root = i
    else:
        tree[parents[i]].append(i)

# 루트 제거면 전체 제거
if remove == root:
    print(0)
    sys.exit()

# 부모의 자식 리스트에서 제거 노드 삭제
for i in range(n):
    if remove in tree[i]:
        tree[i].remove(remove)

leaf_count = 0

def dfs(node):
    global leaf_count
    # 자식이 없으면 리프 노드
    if not tree[node]:
        leaf_count += 1
    else:
        for child in tree[node]:
            dfs(child)

dfs(root)
print(leaf_count)
