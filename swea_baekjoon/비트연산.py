T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0 , -1, 0]

for tc in range(1,T+1):
    N = int(input())
    M = [[0]*N for _ in range(N)]
    d_no = 0
    x, y = 0

    for i in range(1, N**2+1):
        M[x][y] = i
        if x+dx[d_no]





N, M = map(int, input().split())
trees = list(map(int, input().split()))
maximum = max(trees)
baseline = maximum//2

def cut_trees(baseline):
    return sum(tree-baseline for tree in trees if tree > baseline)

def find_maximum_h(M):
    start = 0 
    end = maximum
    result = 0
    while start <= end:
        baseline = (start+end)//2
        m = cut_trees(baseline)
        if m < M:
            end = baseline-1
        else:
            result = baseline
            start = baseline+1
    return result

print(find_maximum_h(M))