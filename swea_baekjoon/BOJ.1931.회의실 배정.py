import sys

input = sys.stdin.readline

n = int(input())
meetings = []
for _ in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))

# 종료 시간 기준으로 정렬 (종료 시간이 같으면 시작 시간이 빠른 순)
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
last_end = 0

# 각 회의를 순회하며 선택 가능하면 선택
for s, e in meetings:
    if s >= last_end:
        count += 1
        last_end = e

print(count)