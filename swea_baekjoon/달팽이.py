T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0 , -1, 0]

for tc in range(1,T+1):
    N = int(input())
    M = [[0]*N for _ in range(N)]
    d_no = 0
    x = y = 0

    for i in range(1, N**2+1):
        M[x][y] = i
        if 0<= x+dx[d_no]< N and 0<= y+dy[d_no]< N:
            if M[x+dx[d_no]][y+dy[d_no]] == 0:
                x = x+dx[d_no]
                y = y+dy[d_no]
            else:
                d_no = (d_no+1)%4
                x = x+dx[d_no]
                y = y+dy[d_no]
        else:
            d_no = (d_no+1)%4
            x = x+dx[d_no]
            y = y+dy[d_no]
            
    print(f'#{tc}')
    for i in range(N):
        for m in M[i]:
            print(f'{m}',end=' ')
        print()