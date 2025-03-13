switch_len = int(input())
switch_list = list(map(int, (input().split())))
number_of_student = int(input())
student_list = [list(map(int, (input().split()))) for i in range(number_of_student)]
# [[성별, 스위치번호], ] 형태의 리스트 받기

def toggle(x):
        return 1-x



for student in student_list: #[성별, 숫자]로 이루어진 학생들 하나씩 받아오기
    if student[0] == 1: #남자
       n = student[1] # 스위치 번호, 배열 번호는 n-1
       while n <= switch_len:
            switch_list[n-1] = toggle(switch_list[n-1])
            n += student[1]
    
    else:
         n = student[1]
         i = 1 
         switch_number_list = [n]
         while (n-1-i>=0) and (n-1+i < switch_len) and (switch_list[n-1-i] == switch_list[n-1+i]):
              switch_number_list += [n-i, n+i]
              i += 1
            

         for ab in switch_number_list:
              switch_list[ab-1] = toggle(switch_list[ab-1])
         
print(switch_list)

n = switch_len
i = 0
while n>0:
     if n < 20:
        for a in range(n):
            print(switch_list[i+a],end=' ')
        break
     else:
        for b in range(20):
            print(switch_list[i+b], end=' ')
            n -= 20
            i += 20
     print()
