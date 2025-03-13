T = int(input())


def bubble_sort(numbers, N):
    for i in range(N-1,0, -1): #횟수에 대한 for문으로 첫번째 항은 N-2까지 왜? +1할거라라
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    bubble_sort(numbers, N)
    print(f'#{tc}',end=' ')
    for number in numbers:
        print(number, end= ' ')
    print()
 


