import sys
sys.stdin = open("input.1859.txt", "r")

T=int(input())
ANS =[]
for tc in range(1,T+1):
    N=int(input())
    Sale_price_list = list(map(int, input().split()))
    profit = 0
    max_value = Sale_price_list[N-1]
    for i in reversed(range(len(Sale_price_list))):    
        if Sale_price_list[i] <= max_value:
            profit += max_value - Sale_price_list[i]
        else:
            max_value = Sale_price_list[i]
    ANS.append(str(profit))    
for i, v in enumerate(ANS):
    print(f'#{i+1} {v}')