# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())

def combination(array, r):
    # 조건 1: 선택할 개수가 0개라면, 빈 리스트를 반환 (조합에 아무것도 포함되지 않음)
    if r == 0:
        return [[]]
    # 조건 2: 배열이 비었는데 선택할 개수가 남아있으면, 조합을 만들 수 없음
    if not array:
        return []
    # 첫 번째 요소를 포함한 
    include_first = combination(array[1:], r - 1)  # 나머지 배열로 재귀 호출
    include_first_result = []
    for comb in include_first:
        include_first_result.append([array[0]] + comb)  # 첫 번째 요소를 추가한 결과 생성
    # 첫 번째 요소를 포함하지 않은
    exclude_first = combination(array[1:], r)  # 나머지 배열로 재귀 호출
    # 두 결과를 합쳐 반환
    return include_first_result + exclude_first

for t in range(1, T + 1):
    ans = float("inf")
    B, S = map(int, input().split())
    H = list(map(int, input().split()))
    for i in range(1,B+1):
        for com in combination(H,i):
            totalH = sum(com)
            if totalH >= S:
                ans = min(ans, totalH-S)
    print(f"#{t} {ans}")