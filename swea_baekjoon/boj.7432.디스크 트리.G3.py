class Node:
    def __init__(self):
        # key: 디렉토리/파일 이름, value: 해당 이름에 해당하는 Node
        self.children = {}
        # 자식의 이름을 사전순 관리하기 위한 힙


N = int(input())

# 루트 노드 (실제 출력에는 등장하지 않는 루트)
root = Node()

# 1) 입력을 받아 트리에 경로 삽입
for _ in range(N):
    path = input().split('\\')  # 역슬래시 기준으로 split
    current = root
    for name in path:
        # 해당 자식 노드가 없으면 새로 만들고
        if name not in current.children:
            current.children[name] = Node()
        # 내려가기
        current = current.children[name]

# 2) 전위순회(재귀)를 이용해 출력
def dfs(node, depth):
    # 현재 노드의 자식을 사전순으로 탐색색
    for child_name in sorted(node.children.keys()):
        # 깊이만큼 공백을 붙여서 출력
        print(" " * depth + child_name)
        dfs(node.children[child_name], depth + 1)

# 루트의 깊이는 0으로 시작
dfs(root, 0)
