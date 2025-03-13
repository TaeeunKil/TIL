T = int(input())
for tc in range(1, 1+T):
    count = 0
    data = input()
    count += data.count('(|')
    count += data.count('()')
    count += data.count('|)')
    print(f'#{tc} {count}')
    