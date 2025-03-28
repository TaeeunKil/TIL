# import sys
# sys.stdin = open('sample_input (30).txt', 'r')

def four_operations(a, b, i):
    if i == 0:
        return a+b
    elif i == 1:
        return a-b
    elif i == 2:
        return a*b
    elif i == 3:
        if a*b < 0:
            return (-1)*(abs(a)//abs(b))
        return a//b


def dfs(cnt, result, select=''):
    global max_ans, min_ans
    
    if cnt == N-1:
        max_ans = max(max_ans, result)
        min_ans = min(min_ans, result)
        # print(f'ans:',select)
        # print(f'result:',result)
        return
    
    for i in range(len(operators)):
        if operators[i] == 0:
            continue
        operators[i] -= 1
        new_select = select + str(i)
        new_result = four_operations(result, digits[cnt+1], i)
        # print('')
        # print(f'select:',select)
        # print(result)
        # print(f'operator', i)
        # print(digits[cnt+1])
        # print('=')
        # print(new_result)
        # print('')
        dfs(cnt+1, new_result, new_select)
        operators[i] += 1
        

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    operators = list(map(int, input().split()))
    digits = list(map(int, input().split()))
    max_ans = float('-inf')
    min_ans = float('inf')
    start = digits[0]
    dfs(0, start)
    print(f'#{tc}', max_ans-min_ans)