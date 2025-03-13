T =10
for tc in range(1, T+1):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    y= ladder[99].index(2)
    x = 99
    dx = [0, 0, -1]
    dy = [1, -1, 0]

    while x > 0:
        ladder[x][y] = 0
        for i in range(3):
            new_y = y+dy[i]
            new_x = x+dx[i]
            if 0 <= new_y < 100 and ladder[new_x][new_y] != 0:
                x = new_x
                y = new_y
                break
    print(f'#{N} {y}')
            
            
        
        