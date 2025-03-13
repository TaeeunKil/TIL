w, h = map(int,input().split())
shop_number = int(input())
shops = []
for _ in range(shop_number):
    shops.append(list(map(int,input().split())))
init_dir, donggeun = map(int, input().split())

changing = [0, 4, 3, 1, 2]

def changing_coord(coord):
    direction, dist = coord
    if direction == 1:
        dist = w - dist

    elif direction == 4:
        dist = h - dist
    
    return (direction,dist)

init_dir, donggeun = changing_coord((init_dir, donggeun))

shops = list(map(changing_coord, shops))

ans = 0

first_dir = changing[init_dir]
second_dir = changing[first_dir]
third_dir = changing[second_dir]

if init_dir == 3 or init_dir == 4:
    w, h = h, w

for shop_dir, distance in shops:  
    if shop_dir == init_dir:
        ans += abs(donggeun - distance)    
    elif shop_dir == second_dir:
        if distance < donggeun:
            ans += distance + w- donggeun + h
        elif distance > donggeun:
            ans += w-distance + donggeun + h
        else:
            ans += w+h
    elif shop_dir == first_dir:
        ans += h-distance + donggeun
    elif shop_dir == third_dir:
        ans += w-donggeun + distance
print(ans)
