T = int(input())
for tc in range(1,T+1):
    heights = list(map(int, input().split()))
    height = max(heights)
    height += 1
    while not height%7 == 0:
        height += 1 
    print(height)