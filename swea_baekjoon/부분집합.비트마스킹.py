powerset = []
n = 9
for _ in range(n):
    powerset.append(int(input()))

for mask in range(1 << n):
    partset = []
    sum_of_partset = 0
    for i in range(n-1, -1, -1):
        if mask & (1 << i):
            partset.append(powerset[i])
            sum_of_partset += powerset[i]
        if sum_of_partset > 100:
            break
    if sum_of_partset == 100 and len(partset)==7:
        break

partset.sort()
for height in partset:
    print(height)