k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(6)]

max_width = 0
max_width_idx = 0
max_height = 0
max_height_idx = 0

for i in range(6):
    direction, length = edges[i]
    if direction == 1 or direction == 2:
        if length > max_width:
            max_width = length
            max_width_idx = i
    else:  # 남, 북 방향
        if length > max_height:
            max_height = length
            max_height_idx = i

# 작은 직사각형의 한 변의 길이는 각각
# (최대 변의 인덱스 + 3) % 6에 해당하는 길이이다.
small_width = edges[(max_width_idx + 3) % 6][1]
small_height = edges[(max_height_idx + 3) % 6][1]

result = k * ((max_width * max_height) - (small_width * small_height))
print(result)