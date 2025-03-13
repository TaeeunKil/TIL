T = int(input())
for tc in range(1, 1+T):
    N, K = map(int, input().split())
    hexa_str = input()
    test_set = set()
    side_no = N//4
    start = 0
    for i in range(side_no):
        start = i
        for j in range(4):
            new_start = start+ j*side_no
            segment = ''
            for k in range(side_no):
                # print((start+k)%N)
                segment += hexa_str[(new_start+k)%N]
            test_set.add(int(segment, 16))
    test_list = list(test_set)
    test_list.sort(reverse=True)
    print(f'#{tc}',test_list[K-1])
