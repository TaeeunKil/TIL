import sys
sys.stdin = open('input.txt', 'r')

N = 4  # 기어 수
M = 8  # 기어 날개 수
gears = [0]*N
pointors = [[0,2,6] for _ in range(N)]
twelve = 0
right = 1
left = 2

def rotate(gear_idx, rotation):

    if rotation == 1:
        rotate_num = 7
    else:
        rotate_num = 1

    for i in range(3):
        pointors[gear_idx][i] += rotate_num
        pointors[gear_idx][i] %= M

for i in range(N):
    gears[i] = input()

# print(gears)

K = int(input())

q = []

for _ in range(K):
    gear_no, rotation = map(int, input().split())
    gear_idx = gear_no - 1
    
    will_be_rotated =[0]*N
    
    visited = [False]*N
    q.append((gear_idx, rotation))
    visited[gear_idx] = True
    
    while q:
        cur_idx, cur_rotation = q.pop(0)
        # print(cur_idx)
        will_be_rotated[cur_idx] = cur_rotation
        left_idx = cur_idx -1
        right_idx = cur_idx + 1
        if left_idx >=0 and not visited[left_idx]:
            # print('left not visited')
            # print('idx',cur_idx, left_idx)
            # print('pointors', pointors[cur_idx][left], pointors[left_idx][right])
            # print(gears[cur_idx][pointors[cur_idx][left]], gears[left_idx][pointors[left_idx][right]])
            if gears[cur_idx][pointors[cur_idx][left]] != gears[left_idx][pointors[left_idx][right]]:
                q.append((left_idx, cur_rotation*(-1)))
                visited[left_idx] = True

        
        if right_idx < N and not visited[right_idx]:
            # print('right not visited')
            # print('idx',cur_idx, right_idx)
            # print('pointors', pointors[cur_idx][right], pointors[right_idx][left])
            # print(gears[cur_idx][pointors[cur_idx][right]], gears[right_idx][pointors[right_idx][left]])
            if gears[cur_idx][pointors[cur_idx][right]] != gears[right_idx][pointors[right_idx][left]]:
                q.append((right_idx, cur_rotation*(-1)))
                visited[right_idx] = True
    
    # print(will_be_rotated)
    
    for gear_idx in range(4):
        if will_be_rotated[gear_idx] == 0:
            continue
        rotate(gear_idx, will_be_rotated[gear_idx])


ans = 0

for gear_i in range(N):
    ans += int(gears[gear_i][pointors[gear_i][twelve]]) *(1<<gear_i)

print(ans)



# GPT 예시

# from collections import deque
# def main():
#     # 톱니바퀴 4개의 초기 상태를 입력받아 deque에 저장
#     gears = [deque(input().strip()) for _ in range(4)]
#     K = int(input().strip())  # 회전 명령의 개수
#     for _ in range(K):
#         idx, direction = map(int, input().split())
#         idx -= 1  # 0-index로 변환
#         # 각 톱니바퀴가 회전할 방향을 저장하는 리스트 (0이면 회전 없음)
#         rotate_directions = [0] * 4
#         rotate_directions[idx] = direction
#         # 왼쪽 톱니바퀴로 전파
#         for i in range(idx, 0, -1):
#             if gears[i][6] != gears[i-1][2]:
#                 rotate_directions[i-1] = -rotate_directions[i]
#             else:
#                 break  # 접촉부가 같으면 연쇄 전파 중단
#         # 오른쪽 톱니바퀴로 전파
#         for i in range(idx, 3):
#             if gears[i][2] != gears[i+1][6]:
#                 rotate_directions[i+1] = -rotate_directions[i]
#             else:
#                 break
#         # 모든 톱니바퀴에 대해 회전 적용
#         for i in range(4):
#             if rotate_directions[i] != 0:
#                 gears[i].rotate(rotate_directions[i])
#     # 최종 점수 계산
#     score = 0
#     for i in range(4):
#         if gears[i][0] == '1':
#             score += (1 << i)
#     print(score)
# if __name__ == '__main__':
#     main()


# 여기서 배운 것 deque.rotate()가 회전을 의미한다.
# 어떤 d = deque(리스트) 일 때 
# d.rotate(2) = 오른쪽으로 2칸 이동, d.rotate(-1) = 왼쪽으로 1칸 이동