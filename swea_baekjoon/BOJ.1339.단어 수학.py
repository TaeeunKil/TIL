from heapq import heappop, heappush

N = int(input())
words = [0]*N
priority = {}


for i in range(N):
    word = input()
    words[i] = word
    max_digit = len(word)-1
    
    for digit_num in range(max_digit+1):
        digit_idx = max_digit-digit_num  # 인덱스는 거꾸로다!
        alphabet = word[digit_idx]
        if not priority.get(alphabet):
            priority[alphabet] = 0
        priority[alphabet] += 10**(digit_num)
    
heap = []

for item in priority.items():
    alpha, prior = item
    heappush(heap, (-prior, alpha))

alphabet_to_num = {}
for i in range(9, -1, -1):
    if heap == []:
        break
    prior, alpha = heappop(heap)
    alphabet_to_num[alpha] = str(i)

ans = 0

for word in words:
    result = ''
    for i in range(len(word)):
        result += alphabet_to_num[word[i]]
    ans += int(result)
    
print(ans)


# def main():
#     import sys
#     input = sys.stdin.readline
#     n = int(input().strip())
#     letter_weight = {}
    
#     # 각 글자가 가지는 자릿수 가중치 계산
#     for _ in range(n):
#         word = input().strip()
#         length = len(word)
#         for i, char in enumerate(word):
#             # 해당 글자의 자릿수에 따른 기여도 (10^(위치))
#             letter_weight[char] = letter_weight.get(char, 0) + 10 ** (length - i - 1)
    
#     # 기여도가 큰 글자부터 높은 숫자를 할당
#     sorted_letters = sorted(letter_weight.items(), key=lambda x: x[1], reverse=True)
#     result = 0
#     current_digit = 9
#     for letter, weight in sorted_letters:
#         result += current_digit * weight
#         current_digit -= 1
    
#     print(result)

# if __name__ == '__main__':
#     main()


# 가중치 딕셔너리 제작
# items로 힙 푸시 해서 정렬 
# 뽑으면서 0~9 사전 제작 
# 단어 읽으면서 숫자 제작

# gpt에서 얻은 것
# letter_weight[char] = letter_weight.get(char, 0) + 10 ** (length - i - 1)
# 한 줄로 없으면 초기화까지 구현
# sorted_letters = sorted(letter_weight.items(), key=lambda x: x[1], reverse=True)
# 한 줄로 정렬을 위한 교환 없이 정렬. 
# 키를 lambda x: x[1], 로 키순서대로 정렬해라
# reverse = True로 큰 순서대로 정렬

