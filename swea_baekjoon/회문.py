

T =1

def palindrome_count(M, N, c):
    for j in range(8):
        for i in range(8-N+1):
            check = M[j][i:i+N]
            print(check)
            reverse_check = check[::-1]
            print(reverse_check)
            if check == reverse_check:
                c += 1
    return c
    

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(input()) for _ in range(8)]
    ans = 0
    ans = palindrome_count(matrix,N,ans)
    column_matrix = list(zip(*matrix))
    ans = palindrome_count(column_matrix,N,ans)

    print(f'#{tc} {ans}')

        
        