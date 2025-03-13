from collections import deque

T = 1

# def solve(num):
#     q=deque()
#     q.append(num)
#     lst[num][0]-=1
 
#     while q:
#         n=q.popleft()
#         result.append(n)
 
#         if len(lst[n])>1:
#             for i in lst[n][1:]:
#                 lst[i][0]-=1
#                 if lst[i][0]==0:
#                     q.append(i)
 
for tc in range(1,T+1):
    V, E=map(int,input().split())
    edges = list(map(int,input().split()))
    degrees = [0]*(V+1)
    adj_list = [[] for _ in range(V+1)]
    result=[]
    zero=[]
    for i in range(0, len(edges)//2):
        start_idx = 2*i
        end_idx = start_idx + 1
        start_node = edges[start_idx]
        end_node = edges[end_idx]
        degrees[end_node] += 1
        adj_list[start_node].append(end_node)
    print(degrees)
    print(adj_list)
        
     
    for i in range(1,V+1):
        if adj_list[i] == []:
            zero.append(i)
 
    # for i in zero:
    #     solve(i)
    
    # print(f'#{tc} '+ ' '.join(map(str,result)))