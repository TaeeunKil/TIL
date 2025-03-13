T = int(input())

def is_okay(candies):
    candy_0 = candies[0]
    candy_1 = candies[1]
    candy_2 = candies[2]
    if candy_0 < candy_1 < candy_2:
        return 0   
    if candy_1 < 2 or candy_2 < 3:
        return -1
    ans = 0
    if candy_1 >= candy_2:
        ans = candy_1 - candy_2 + 1
        candy_1 -= ans
    if candy_0 >= candy_1:
        ans += candy_0 - candy_1 +1
    return ans


for tc in range(1, T+1):
    candies= list(map(int, input().split()))
    print(f'#{tc}', is_okay(candies))