N, M = map(int, input().split())
trees = list(map(int, input().split()))
maximum = max(trees)


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