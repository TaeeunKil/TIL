T = int(input())

dr = [1,  1, -1, -1]
dc = [1, -1, -1,  1]

def get_path(r, c, d1, d2):
    path = []
    sides = [d1, d2, d1, d2]
    cur_r, cur_c = r, c

    for i in range(4):
        side = sides[i]
        for _ in range(side):
            cur_r += dr[i]
            cur_c += dc[i]

            if not(0 <= cur_r < N and 0 <= cur_c < N):
                return False
            path.append((cur_r, cur_c))

    if (cur_r, cur_c) != (r, c):
        return False

    return path

for tc in range(1, T + 1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    ans = -1  

    for r in range(N):
        for c in range(N):
            for d1 in range(1, N):
                for d2 in range(1, N):
                    #꼭짓점이 바깥으로 나갈 경우 제외
                    #4번째는 자기 자신이라 제외
                    if not (0 <= r + d1 < N and 0 <= c + d1 < N):
                        continue
                    if not (0 <= r + d1 + d2 < N and 0 <= c + d1 - d2 < N):
                        continue
                    if not (0 <= r + d2 < N and 0 <= c - d2 < N):
                        continue

                    path = get_path(r, c, d1, d2)
                    if path == False:
                        continue

                    dessert_set = set()
                    is_impossible = False
                    for coord in path:
                        x, y = coord
                        dessert = cafe[x][y]
                        if dessert not in dessert_set:
                            dessert_set.add(cafe[x][y])
                        else:
                            is_impossible = True
                            break
                    if is_impossible:
                        continue
                    

                    ans = max(ans, len(path))

    print(f"#{tc} {ans}")