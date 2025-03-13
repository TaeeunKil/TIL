N, S = map(int,input().split())
numbers = list(map(int, input().split())) +[0]
start = 0
end = 0
cur_sum = 0
ans = float('inf')


while end != N+1:
    
    if cur_sum >= S:
        ans = min(ans, end-start)
        cur_sum -= numbers[start]
        start += 1
    
    else:
        cur_sum += numbers[end]
        end += 1

if ans == float('inf'):
    ans = 0

print(ans)



# 설계
# start = 0, end = 1로 설정해서 슬라이싱을 계속 해가자
# 슬라이싱용 인덱스니까 end가 넘어가는 경우 고려해야하니까 numbers+[0]로 만들자

# +1씩 하는 조건을 나눠야한다
#  end를 부분합이 S가 넘을때까지 +1
# 넘으면 start를 +1

# 만약 start == N-1, end == N 이 되면 종료 << 틀렸음

# 그냥 end가 N 이상이 되는 순간 멈춰도 된다. 
# 왜냐하면 더 큰 부분합을 찾으러 가는건데 더 이상 더할 값이 없을 때가 그떄. << 또 틀렸다(후에 수정)

# 또 문제 발생 슬라이싱의 시간복잡도가 k여서
# O(n^2)이 되는 이유로 시간초과가 발생했다
# 따라서 슬라이싱을 하지 않고 그냥 현재 합을 계속 갱신해가는 방향으로 수정
# 슬라이싱용 인덱스를 수정함에 따라 end = 0에서 시작하는 걸로 수정하고 
# numbers+[0]을 numbers로 수정

# 최솟값 비교라 ans = inf로 초기화 했는데 
# while 돌입 안하면 inf로 출력되니까 0으로 바꾸는 로직 추가

# while 조건이 잘못되었다는 사실을 발견
# end = N이어도 cur_sum>=S 이면 start를 하나 당겨서 최소인지 확인을 해줘야한다 이 경우를 생각안함
# 그래서 다시 numbers에 0을 하나 추가하고 N+1일때 멈추게 해서 
# 인덱스 에러를 방지하고 start를 한 바퀴 더 돌게 했다.