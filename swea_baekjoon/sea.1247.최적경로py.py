from itertools import permutations

def make_distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    xy = list(map(int, input().split()))
    q = []
    # company_x = xy[0]
    # company_y = xy[1]
    # home_x = xy[2]
    # home_y = xy[3]
    adj_matrix = [[0]*(N+2) for _ in range(N+2)]
    for i in range(N+2):
        x1 = xy[2*i]
        y1 = xy[2*i+1]        
        for j in range(N+2):
            if i == j:
                continue
            x2 = xy[2*j]
            y2 = xy[2*j+1]
            d = make_distance(x1,y1,x2,y2)
            adj_matrix[i][j] = d
            adj_matrix[j][i] = d
            
    ans = float('inf')
    
    for per in permutations(range(2, N+2), N):
        result = 0
        per = [0] + list(per) + [1]
        for i in range(N+1):
            result += adj_matrix[per[i]][per[i+1]]
        ans = min(ans, result)
    print(f'#{tc}', ans)