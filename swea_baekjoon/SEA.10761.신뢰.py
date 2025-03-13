T = int(input())

for tc in range(1, 1+T):
    bottons = list(input().split())
    N = int(bottons.pop(0))
    robot = bottons[::2]
    botton_no = list(map(int, bottons[1::2]))
    cur_o = 1
    cur_b = 1

    last_o = 0
    last_b = 0

    needed = 0
    for i in range(N):
        if robot[i] == 'B':
            #흐른 시간
            flow = needed - last_b
            #거리
            d = abs(botton_no[i] - cur_b)
            #더 필요한 시간
            add = max(0, d-flow)
            needed += add +1
            cur_b = botton_no[i]
            last_b = needed            
        else: 
            flow = needed - last_o
            distance = abs(botton_no[i] - cur_o)
            additional = max(0, distance - flow)
            needed += additional + 1
            cur_o = botton_no[i]
            last_o = needed
    
    print(f'#{tc} {needed}')