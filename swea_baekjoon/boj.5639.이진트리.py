import sys
sys.stdin = open("input_5639.txt", "r")

preorder = []
while True:
    try:
        line = int(input())
    except Exception:  # 모든 일반적인 예외를 잡습니다.
        break
    preorder.append(line)

def preorder_to_postorder_optimized(preorder):
    postorder = []
    idx = 0

    def helper(bound):
        nonlocal idx
        # 인덱스가 범위를 벗어나거나, 현재 값이 상위 노드의 경계보다 크면 해당 서브트리 없음
        if idx >= len(preorder) or preorder[idx] > bound:
            return
        
        root_val = preorder[idx]
        idx += 1
        
        # 현재 노드를 기준으로 왼쪽 서브트리 처리 (경계는 현재 노드의 값)
        helper(root_val)
        # 오른쪽 서브트리 처리 (경계는 상위 호출로부터 받은 bound)
        helper(bound)
        
        # 후위순회: 왼쪽, 오른쪽, 루트 순으로 저장
        postorder.append(root_val)

    helper(float('inf'))
    return postorder
postorder = preorder_to_postorder_optimized(preorder)

for node in postorder:
    print(node)