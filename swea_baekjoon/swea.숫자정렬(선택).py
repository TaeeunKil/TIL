T = int(input())


def selection_sort(numbers, N):
    for i in range(N-1):  #탐색구간의 첫번쨰 인덱스가 될 것
        min_index = i #최초값을 최솟값으로 가정하고 인덱스 받기
        for j in range(i+1, N):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    selection_sort(numbers, N)
    print(f'#{tc}',end=' ')
    for number in numbers:
        print(number, end= ' ')
    print()
 


