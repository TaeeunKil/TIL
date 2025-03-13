
T = int(input())
N = 3

def clockwise(mylist):
    return list(map(list, zip(*mylist[::-1])))


def counter_clockwise(mylist):
    return list(map(list, zip(*mylist)))[::-1]


def turning(reference, direction):
    global L
    global U
    global F
    global D
    global B
    global R

    if reference == 'U':
        if direction == '+':
            U = clockwise(U)
            for i in range(N):
                f, l, b, r = F[0][i], L[i][2], B[2][abs(i-2)], R[abs(i-2)][0]
                F[0][i], L[i][2], B[2][abs(i-2)], R[abs(i-2)][0] = r, f, l, b

        
        elif direction == '-':
            U = counter_clockwise(U)
            for i in range(N):
                f, l, b, r = F[0][i], L[i][2], B[2][abs(i-2)], R[abs(i-2)][0]
                F[0][i], L[i][2], B[2][abs(i-2)], R[abs(i-2)][0] = l, b, r, f 
    
    elif reference == 'D':
        if direction == '+':
            D = clockwise(D)
            for i in range(N):
                f, r, b, l = F[2][i], R[abs(i-2)][2], B[0][abs(i-2)], L[i][0]
                F[2][i], R[abs(i-2)][2], B[0][abs(i-2)], L[i][0] = l, f, r, b
        
        elif direction == '-':
            D = counter_clockwise(D)
            for i in range(N):
                f, r, b, l = F[2][i], R[abs(i-2)][2], B[0][abs(i-2)], L[i][0]
                F[2][i], R[abs(i-2)][2], B[0][abs(i-2)], L[i][0] = r, b, l, f
                

    elif reference == 'L':
        
        if direction == '+':
            L = clockwise(L)
            for i in range(N):
                f, u, b, d = F[i][0], U[i][0], B[i][0], D[i][0]
                F[i][0], U[i][0], B[i][0], D[i][0] = u, b, d, f

        if direction == '-':
            L = counter_clockwise(L)
            for i in range(N):
                f, u, b, d = F[i][0], U[i][0], B[i][0], D[i][0]
                F[i][0], U[i][0], B[i][0], D[i][0] = d, f, u, b

    elif reference == 'R':
        if direction == '+':
            R = clockwise(R)
            for i in range(N):
                u, b, d, f = U[i][2], B[i][2], D[i][2], F[i][2]
                U[i][2], B[i][2], D[i][2], F[i][2] = f, u, b, d
        
        elif direction == '-':
            R = counter_clockwise(R)
            for i in range(N):
                u, b, d, f = U[i][2], B[i][2], D[i][2], F[i][2]
                U[i][2], B[i][2], D[i][2], F[i][2] = b, d, f, u
    
    elif reference == 'F':
        if direction == '+':
            F = clockwise(F)
            for i in range(N):
                u, r, d, l = U[2][i], R[2][i], D[0][abs(i-2)], L[2][i]
                U[2][i], R[2][i], D[0][abs(i-2)], L[2][i] = l, u, r, d
        
        elif direction == '-':
            F = counter_clockwise(F)
            for i in range(N):
                u, r, d, l = U[2][i], R[2][i], D[0][abs(i-2)], L[2][i]
                U[2][i], R[2][i], D[0][abs(i-2)], L[2][i] = r, d, l, u
    
    elif reference == 'B':
        if direction == '+':
            B = clockwise(B)
            for i in range(N):
                u, r, d, l = U[0][i], R[0][i], D[2][abs(i-2)], L[0][i]
                U[0][i], R[0][i], D[2][abs(i-2)], L[0][i] = r, d, l, u

        elif direction == '-':
            B = counter_clockwise(B)
            for i in range(N):
                u, r, d, l = U[0][i], R[0][i], D[2][abs(i-2)], L[0][i]
                U[0][i], R[0][i], D[2][abs(i-2)], L[0][i] = l, u, r, d
    



for tc in range(1,T+1):
    U = [['w']*3 for _ in range(N)] #U 0
    L = [['g']*3 for _ in range(N)] #L 1
    F = [['r']*3 for _ in range(N)] #F 2
    D = [['y']*3 for _ in range(N)] #D 3
    R = [['b']*3 for _ in range(N)] #R 4
    B = [['o']*3 for _ in range(N)] #B 5
    

    n = int(input())
    turnning_cube = list(input().split())
    for turn in turnning_cube:
        turning_posit, turning_dir = list(turn)
        turning(turning_posit, turning_dir)
    
   
    for row in U:
        ans=''
        for a in row:
            ans += a
        print(ans)
    