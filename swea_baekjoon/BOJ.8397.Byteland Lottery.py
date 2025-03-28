l = int(input())
w = list(map(int, input().split()))

# 모든 w가 0이면, (1+0)=1을 곱해 P=1, P-1=0이 되어 디지털 루트는 0입니다.
if all(x == 0 for x in w):
    print(0)
else:
    mod = 9
    prod_mod = 1
    for x in w:
        # (1 + x)를 9로 모듈러 연산하며 곱합니다.
        prod_mod = (prod_mod * ((x + 1) % mod)) % mod

    # 전체 합은 prod(1+w) - 1 이므로, 모듈러 연산에서는 (prod_mod - 1) % 9가 됩니다.
    result_mod = (prod_mod - 1) % mod

    # result_mod가 0이지만, 실제 P-1이 0이 아니라면 디지털 루트는 9입니다.
    if result_mod == 0:
        print(9)
    else:
        print(result_mod)
