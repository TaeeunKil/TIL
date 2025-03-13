from collections import deque
from copy import deepcopy
from pprint import pprint


N, M= map(int, input().split())
board = [list(input()) for _ in range(N)]

directions = [(1,0), (0,1), (0,-1), (-1,0)]

for i in range(N):
    for j in range(M):
        value = a[i][j]
        if value == 'R':
            red_coord = [i,j]
            board[i][j] = '.'
        elif value == 'B':
            blue_coord = [i,j]
            board[i][j] = '.'
        elif value == 'O':
            hole_coord = [i,j]



def beads_bfs(red, blue):
    global board
    q = deque()
    visited = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)] # 4차원으로 구성해야 rr rc이 같아도 br bc가 다르면 다른 상태
    q.append([red, blue, 0])
    rr, rc = red
    br, bc = blue
    visited[rr][rc][br][bc] = 1

    while q:
        l = len(q)
        for _ in range(l):
            r, b, turn = q.popleft()
            if turn > 10:
                return -1
            for dr, dc in directions:
                cur_rr, cur_rc = r
                cur_br, cur_bc = b

                priority = 0
                if dr == 1 and cur_br > cur_rr:
                    priority = 1                   
                elif dc == 1 and cur_bc > cur_rc:
                    priority = 1
                elif dr == -1 and cur_br < cur_rr:
                    priority = 1
                elif dc == -1 and cur_bc < cur_rc:
                    priority = 1
                
                
                if priority == 0: #red 먼저
                    board[cur_rr][cur_rc] = '.'
                    red_meet_O = False
                    while True:
                        new_rr, new_rc = cur_rr+dr, cur_rc+dc
                        
                        if board[new_rr][new_rc] == '.':
                            cur_rr, cur_rc = new_rr, new_rc
                            continue
                        elif board[new_rr][new_rc] == 'O':
                            red_meet_O = True
                            break
                        break
                    
                    if not red_meet_O:
                        board[cur_rr][cur_rc] = 'R'
                    

                    board[cur_br][cur_bc] = '.'
                    blue_meet_O = False

                    while True:
                        new_br, new_bc = cur_br+dr, cur_bc+dc
                        
                        if board[new_br][new_bc] == '.':
                            cur_br, cur_bc = new_br, new_bc
                            continue
                        elif board[new_br][new_bc] == 'O':
                            blue_meet_O = True
                            break
                        break
                    board[cur_br][cur_bc] = 'B'
                    if blue_meet_O:
                        continue

                    if red_meet_O:
                        return turn + 1

                    if visited[cur_rr][cur_rc][cur_br][cur_bc]:
                        continue

                    
                    q.append([[cur_rr, cur_rc], [cur_br, cur_bc], turn+1, board])
                    visited[cur_rr][cur_rc][cur_br][cur_bc] = 1
                    
                
                elif priority == 1: #blue 먼저

                    board[cur_br][cur_bc] = '.'
                    blue_meet_O = False

                    while True:
                        
                        new_br, new_bc = cur_br+dr, cur_bc+dc
                        if board[new_br][new_bc] == '.':
                            cur_br, cur_bc = new_br, new_bc
                            continue
                        elif board[new_br][new_bc] == 'O':
                            blue_meet_O = True
                            break
                        break
                    
                    if blue_meet_O:
                        continue
                    
                    board[cur_br][cur_bc] = 'B'

                    board[cur_rr][cur_rc] = '.'

                    while True:
                        new_rr, new_rc = cur_rr+dr, cur_rc+dc
                        if board[new_rr][new_rc] == '.':
                            cur_rr, cur_rc = new_rr, new_rc
                            continue
                        elif board[new_rr][new_rc] == 'O':
                            return turn + 1
                        break
                    board[cur_rr][cur_rc] = 'R'

                    if visited[cur_rr][cur_rc][cur_br][cur_bc]:
                        continue

                    q.append([[cur_rr, cur_rc], [cur_br, cur_bc], turn+1, board])
                    visited[cur_rr][cur_rc][cur_br][cur_bc] = 1
    return -1

print(beads_bfs(red_coord, blue_coord))

