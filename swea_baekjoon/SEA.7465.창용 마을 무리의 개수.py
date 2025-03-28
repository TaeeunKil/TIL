T = int(input())

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    a = find(x)
    b = find(y)
    if a>b:
        parents[a] = b
    elif a<b:
        parents[b] = a
    else:
        return

for tc in range(1, T+1):
    N, M = map(int, input().split())
    parents = list(range(N+1))
    check_set = set()
    for _ in range(M):
        a, b = map(int,input().split())
        union(a, b)
    for i in range(1,1+N):
        union(parents[i], i)
        check_set.add(parents[i])
          
    ans = len(check_set)
    print(f'#{tc}', ans)