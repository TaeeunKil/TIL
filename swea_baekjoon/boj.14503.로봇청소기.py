N, M = map(int, input().split())
cur_position = list(map(int, input().split()))
room = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# (d+3)%4
def is_clean_in_four_direction(r, c):
    for dir in range(len(dr)):
        new_r, new_c = r + dr[dir], c + dc[dir]
        if 0<=new_r<N and 0<=new_c<M:
            if room[new_r][new_c] == 0:
                return False
    return True

ans = 0

while True:
    cur_r, cur_c, direction = cur_position

    if room[cur_r][cur_c] == 0:
        room[cur_r][cur_c] = 2
        ans +=1
    if is_clean_in_four_direction(cur_r, cur_c):
        backward = (direction+2)%4
        back_r, back_c = cur_r + dr[backward], cur_c + dc[backward] 

        if room[back_r][back_c] == 1:
            break
        else:
            cur_position = (back_r, back_c, direction)

    elif not is_clean_in_four_direction(cur_r, cur_c):
        counter_clockwise = (direction+3)%4
        facing_r, facing_c = cur_r + dr[counter_clockwise], cur_c + dc[counter_clockwise]

        if room[facing_r][facing_c] == 0:
            cur_position = (facing_r, facing_c, counter_clockwise)
            continue
        cur_position = (cur_r, cur_c, counter_clockwise)

print(ans)
