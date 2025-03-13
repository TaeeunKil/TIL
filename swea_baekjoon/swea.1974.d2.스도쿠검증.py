T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    ans = 1 # 스도쿠가 맞으면 1 않으면 0
    sdoku_matrix = []
    collect_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        sdoku_matrix.append(list(map(int, input().split())))
    for i in range(9):
        if sorted(sdoku_matrix[i]) != collect_list:
            ans = 0            
            break
        elif sorted([sdoku_matrix[n][i] for n in range(9)]) != collect_list:
            ans = 0
            break
        elif sorted([sdoku_matrix[k+(i-i%3)][j%3+(i%3)*3] for k in range(3) for j in range(3)]) != collect_list:
            ans = 0
            break
    print(f'#{test_case} {ans}')


