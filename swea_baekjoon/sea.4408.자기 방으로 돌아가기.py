# T = int(input())
# M = 200 # 방번호를 압축하자. 왜? 사실상 1,2 3,4 같은 번호임
# for tc in range(1, T+1):
#     N = int(input())
#     starts_ends = [0]*N
#     dis_list = [0]*N
#     for i in range(N):
#         start, end = map(int, input().split())
#         if start > end:
#             start, end = end, start
#         if start % 2 == 0:
#             start = start//2
#         else:
#             start = start//2 +1
#         if end % 2 == 0:
#             end = end//2
#         else:
#             end = end//2 +1
#         dis_list[i] = (end, i)
#         starts_ends[i] = (start, end)
#     dis_list.sort()
#     ans = 0
#     used_dis = [0]*N
#     while not all(used_dis):
#         ans += 1
#         now_used = [0]*(M+1)
#         for i in range(N):
#             cur_dis, cur_i = dis_list[i]
#             cur_start, cur_end = starts_ends[cur_i]
            
#             if used_dis[cur_i] == 1:
#                 continue
            
#             is_used = False
#             for j in range(M+1):
#                 if now_used[j] == 1 and cur_start<= j <= cur_end:
#                     is_used =True
#                     break
#             if is_used:
#                 continue
            
#             used_dis[cur_i] = 1
#             for k in range(cur_start, cur_end+1):
#                 now_used[k] = 1
        
        
#     print(f'#{tc}', ans)
    
    
    
    
T = int(input())
M = 200
for tc in range(1, T+1):
    N = int(input())
    # 복도 번호 압축 후 최대 번호는 200까지이므로, 202정도면 충분함 (인덱스 b+1 때문에)
    student_visited = [0] * (M+1)
    for _ in range(N):
        start, end = map(int, input().split())
        # 방 번호가 역순으로 주어지는 경우를 대비해 정렬
        if start > end:
            start, end = end, start
            
        if start % 2 == 0:
            start = start//2
        else:
            start = start//2 +1
            
        if end % 2 == 0:
            end = end//2
        else:
            end = end//2 +1
        for i in range(start, end+1):
            student_visited[i] +=1
    result = max(student_visited)
    print(f'#{tc} {result}')
