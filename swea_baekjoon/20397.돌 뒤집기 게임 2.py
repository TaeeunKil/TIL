T=int(input())
for tc in range(T):
  N, M = map(int, input().split())
  stones = list(map(int, input().split()))
  for k in range(M):
    i, j = map(int, input().split())
    i = i-1
    for switch in range(1, j+1):
      right = i+switch
      left = i-switch
      if right>=N or left<0:
        break
      if stones[right] == stones[left]:
        stones[right] = 1 - stones[right]
        stones[left] = 1 -stones[left]
  print(f'#{tc}', end = ' ')
  for stone in stones:
    print(stone, end = ' ')
  print()
