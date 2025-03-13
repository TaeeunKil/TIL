T = int(input())

dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

def dfs_clockwise(x, y, dir_index ,steps ,rotate=0):
    global ans
    next_dir_index = (dir_index+1)%4
    new_x = x + dx[next_dir_index]
    new_y = y + dy[next_dir_index]
    if rotate >= 4:
        return
    
    if rotate == 3:
        if dir_index == 0 or dir_index == 2:
            if x-y != start_minus_slope:
                return
            else:
                if (x,y) == (start_x, start_y):
                    if ans < steps:
                        ans = steps
                    return
        else:
            if x+y != start_plus_slope:
                return
            else:
                if (x,y) == (start_x, start_y):
                    if ans < steps:
                        ans = steps
                    return
    
    new_x = x + dx[dir_index]
    new_y = y + dy[dir_index]
    
    if 0<= new_x<N and 0<= new_y<N:
        n = cafe[new_x][new_y]
        
        if not visited[n]:
            visited[n] = 1
            dfs_clockwise(new_x, new_y, dir_index, steps+1, rotate)
            visited[n] = 0

    next_dir_index = (dir_index+1)%4
    new_x = x + dx[next_dir_index]
    new_y = y + dy[next_dir_index]    
    if 0<= new_x<N and 0<= new_y<N:
        m = cafe[new_x][new_y]
        
        if not visited[m]:
            visited[m] = 1
            dfs_clockwise(new_x, new_y, next_dir_index, steps+1, rotate+1)
            visited[m] = 0

        
    


for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*101 #노드가 아닌 숫자 체크용
    ans = -1 
        
    

    for start_x in range(N):
        for start_y in range(N):
            start_minus_slope = start_x - start_y
            start_plus_slope = start_x + start_y
            start_no = cafe[start_x][start_y]
            for i in range(len(dx)):
                new_x = start_x+dx[i]
                new_y = start_y+dy[i]
                check_x = start_x+dx[(i+1)%4]
                check_y = start_y+dy[(i+1)%4]
                if 0<= new_x<N and 0<= new_y<N:
                    if 0<= check_x<N and 0<= check_y<N:
                        new = cafe[new_x][new_y]
                        if not visited[new]:
                            visited[new] = 1
                            dfs_clockwise(new_x, new_y, i, 1)
                            visited[new] = 0


    print(f'#{tc} {ans}') 