T = int(input())
for tc in range(1, T+1):
    M = 13
    day, month, three_month, year = map(int,input().split())
    swimming_days = [0] + list(map(int, input().split()))
    day_month_min_list = [0]*M
    for i in range(1, M):
        day_month_min_list[i] = min(day*swimming_days[i], month)
    print(day_month_min_list)
    money_list = [0]*(M+1)
    money_list[M] = year
    money_list[0] = sum(day_month_min_list)
    for i in range(1, M):
        money_list[i] += three_month
        print(money_list)
        for j in range(1, M):
            if j == i or j == i+1 or j == i+2:
                continue
            money_list[i] += day_month_min_list[j]
    
    print(money_list) 
    print(min(money_list))
# 설계
# 12월까지 min(1일, 1달) 요금으로 M=13으로 최소 기록 리스트 하나 만들기
# 전체 요금 리스트를 M+1 = 14로 하나 더 만들기
# 13번에는 1년 이용권의 가격을 기록
# 0번에는 3달 이용권을 사용하지 않은 sum(최소 기록 리스트)를 기록
# 1월부터 12월까지 시작달의 의미로 3달 요금을 사용했을 때를 또 제작
## 여기서 문제. 3달 요금을 여러번 사용하는 법?
## 이거 dp 마렵다
# 2번째 리스트를 min 하면 값
