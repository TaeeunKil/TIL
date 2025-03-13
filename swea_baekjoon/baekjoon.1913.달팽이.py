N = int(input())
n = int(input())
M = [[0]*N for _ in range(N)] # 0으로 된 빈 행렬 생성

x=N//2
y=N//2
a=1
M[x][y] = a #초기조건들

for i in range(1,N):
    if i%2 == 1:
        for _ in range(i):
            a=a+1
            x=x-1
            M[x][y] = a
        for _ in range(i):
            a=a+1
            y=y+1
            M[x][y] = a
    elif i%2 == 0:
        for _ in range(i):
            a=a+1
            x=x+1
            M[x][y] = a
        for _ in range(i):
            a=a+1
            y=y-1
            M[x][y] = a
    else:
        pass
    if i == N-1:
        for _ in range(i):
            a=a+1
            x=x-1
            M[x][y] = a
ans = [(i,j) for i in range(N) for j in range(N) if M[i][j] == n]

for i in range(N):
    for j in range(N):
        print(M[i][j], end=' ')
    print()

print(f'{ans[0][0]+1} {ans[0][1]+1}')