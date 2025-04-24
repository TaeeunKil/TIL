T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    on_bits = (1<<N)-1
    result = M & on_bits
    ans = ''
    if result == on_bits:
        ans = 'ON'
    else:
        ans = 'OFF'


    print(f'#{tc} {ans}')
