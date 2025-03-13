def matrix_fill_rotation(M):    
    x=0
    y=0
    a=1
    N = len(M)
    M[x][y] = a 
    for _ in range(1,N):
        a += 1
        y += 1
        M[x][y] = a
    # 초기조건들
    # 첫줄을 채우는 이유는 2번씩 반복하면 되는 걸 처음에만 3번돌아서 빼놓음
 
    for i in range(N-1,0,-1):
        if i%2 != N%2:
            for _ in range(i):
                a += 1
                x += 1
                M[x][y] = a
            for _ in range(i):
                a += 1
                y -= 1
                M[x][y] = a        
        else:
            for _ in range(i):
                a += 1
                x -= 1
                M[x][y] = a           
            for _ in range(i):
                a += 1
                y += 1
                M[x][y] = a
    return M

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    matrix0 = [[0]*N for _ in range(N)] # 0으로 된 빈 행렬 생성
    ANS = matrix_fill_rotation(matrix0)
    print(f'#{test_case}')
    for i in range(N):
        print(f"{' '.join(map(str, ANS[i]))}")
 
